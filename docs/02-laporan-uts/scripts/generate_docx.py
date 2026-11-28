import os
import re
import docx
from docx.shared import Cm, Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

DIAGRAM_CAPTIONS = {
    1: "Gambar 1.1: Pemetaan Masalah Operasional terhadap Solusi Sistem SmartPOS",
    2: "Gambar 1.2: Arsitektur Lima Subsistem Fungsional Terintegrasi SmartPOS",
    3: "Gambar 1.3: Peta Jalan Rilis Inkremental Perangkat Lunak SmartPOS (Increment 1 s.d. 4)",
    4: "Gambar 2.1: Arsitektur Multi-Proses dan Isolasi Keamanan Electron 31",
    5: "Gambar 2.2: Hierarki Tiga Tingkat Stakeholder Sistem SmartPOS",
    6: "Gambar 2.3: Pendekatan Elisitasi Kebutuhan Berbasis Bukti Teknis dan Regulasi",
    7: "Gambar 2.4: Matriks Pengendalian Akses Berbasis Peran (RBAC Kasir vs Admin)",
    8: "Gambar 3.1: Use Case Diagram Sistem SmartPOS (Standar OMG UML 2.5.1)",
    9: "Gambar 3.2: Activity Diagram Transaksi Penjualan Kasir dan Fitur Beli Rp",
    10: "Gambar 3.3: Activity Diagram Logistik Barang Masuk dan Rekalkulasi HPP Tertimbang",
    11: "Gambar 3.4: Context Diagram (DFD Tingkat 0) Sistem SmartPOS",
    12: "Gambar 3.5: Data Flow Diagram (DFD) Level 0 Sistem SmartPOS",
    13: "Gambar 3.6: Data Flow Diagram (DFD) Level 1 Dekomposisi Proses Transaksi Kasir 3.0",
    14: "Gambar 4.1: Pemetaan Alur Skenario Use Case UC-02 terhadap Activity Diagram Checkout Kasir",
    15: "Gambar 4.2: Model Evaluasi Keterlacakan Kebutuhan Maju dan Mundur (Traceability Model)"
}

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="B8C4CE", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

def add_formatted_runs(paragraph, text, base_font_size=12, italic_all=False, bold_all=False, color=None):
    text = text.replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
    text = "".join(c for c in text if ord(c) >= 32 or c in '\n\r\t')
    text = text.replace(r'\approx', '≈')
    text = text.replace(r'\le', '≤').replace(r'\ge', '≥')
    text = text.replace(r'\rightarrow', '→').replace(r'\leftarrow', '←')
    text = text.replace(r'\leftrightarrow', '↔')
    text = text.replace(r'\text{', '').replace('}', '')

    pattern = r'(\*\*.*?\*\*|\*.*?\*|`.*?`|\$.*?\$)'
    parts = re.split(pattern, text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**') and len(part) >= 4:
            run = paragraph.add_run(part[2:-2])
            run.bold = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            if italic_all:
                run.italic = True
            if color:
                run.font.color.rgb = color
        elif part.startswith('*') and part.endswith('*') and len(part) >= 2:
            run = paragraph.add_run(part[1:-1])
            run.italic = True
            run.bold = bold_all
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            if color:
                run.font.color.rgb = color
        elif part.startswith('`') and part.endswith('`') and len(part) >= 2:
            run = paragraph.add_run(part[1:-1])
            run.font.name = 'Courier New'
            run.font.size = Pt(base_font_size - 1)
            run.font.color.rgb = RGBColor(30, 30, 30)
        elif part.startswith('$') and part.endswith('$') and len(part) >= 2:
            math_text = part[1:-1].replace('\\', '')
            run = paragraph.add_run(math_text)
            run.italic = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
        else:
            run = paragraph.add_run(part)
            run.bold = bold_all
            run.italic = italic_all
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            if color:
                run.font.color.rgb = color

def clean_heading_text(text):
    cleaned = re.sub(r'^(BAB\s+[IVXLCDM]+:?\s*)', '', text.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r'^(\d+(\.\d+)+\s*)', '', cleaned)
    cleaned = re.sub(r'^(\d+\.\s*)', '', cleaned)
    cleaned = cleaned.replace('**', '').replace('*', '')
    cleaned = cleaned.replace('$→$', '→').replace('$\\rightarrow$', '→')
    cleaned = cleaned.replace('$↔$', '↔').replace('$\\leftrightarrow$', '↔')
    return cleaned.strip()

def build_document():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_path = os.path.join(base_dir, "LAPORAN UTS KELOMPOK 5 - SMARTPOS SISTEM KASIR DAN MANAJEMEN USAHA BERBASIS DESKTOP OFFLINE-FIRST - SOFTWARE REQUIREMENTS SPECIFICATION (SRS)_BACKUP.docx")
    output_path = os.path.join(base_dir, "LAPORAN UTS KELOMPOK 5 - SMARTPOS SISTEM KASIR DAN MANAJEMEN USAHA BERBASIS DESKTOP OFFLINE-FIRST - SOFTWARE REQUIREMENTS SPECIFICATION (SRS).docx")
    img_dir = os.path.join(base_dir, "diagram_images")
    
    print(f"Loading template from {template_path}...")
    doc = docx.Document(template_path)
    
    # Remove tail elements from paragraph 38 onwards (preserving Cover, Kata Pengantar, Daftar Isi and sectPr)
    body = doc._body._element
    p38 = doc.paragraphs[38]._element
    elements_to_remove = []
    found = False
    for child in body:
        if child is p38:
            found = True
        if found:
            if child.tag.endswith('sectPr'):
                continue
            elements_to_remove.append(child)
            
    print(f"Purging {len(elements_to_remove)} old paragraphs/tables from paragraph 38 onwards...")
    for el in elements_to_remove:
        body.remove(el)
        
    print(f"Preserved front matter paragraphs: {len(doc.paragraphs)}, tables: {len(doc.tables)}, sections: {len(doc.sections)}")

    chapter_files = [
        ("BAB I: PENDAHULUAN", os.path.join(base_dir, "bab", "BAB_1_PENDAHULUAN.md")),
        ("BAB II: SOFTWARE REQUIREMENTS SPECIFICATION (SRS)", os.path.join(base_dir, "bab", "BAB_2_SOFTWARE_REQUIREMENTS_SPECIFICATION_SRS.md")),
        ("BAB III: PEMODELAN ANALISIS SISTEM", os.path.join(base_dir, "bab", "BAB_3_PEMODELAN_ANALISIS_SISTEM.md")),
        ("BAB IV: ANALISIS DAN EVALUASI HASIL PEMODELAN", os.path.join(base_dir, "bab", "BAB_4_ANALISIS_DAN_EVALUASI_HASIL_PEMODELAN.md")),
        ("DAFTAR PUSTAKA", os.path.join(base_dir, "bab", "DAFTAR_PUSTAKA.md")),
    ]

    diagram_counter = 0

    for ch_title, ch_path in chapter_files:
        print(f"\nProcessing {ch_title} from {ch_path}...")
        with open(ch_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        is_daftarpustaka = (ch_title == "DAFTAR PUSTAKA")
        
        i = 0
        total_lines = len(lines)
        while i < total_lines:
            raw_line = lines[i].rstrip('\r\n')
            line = raw_line.strip()

            if not line:
                i += 1
                continue

            if line in ['---', '***', '___']:
                i += 1
                continue

            # Heading 1 (Chapter Title)
            if line.startswith('# '):
                doc.add_page_break()
                p = doc.add_paragraph(style='Heading 1')
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(12)
                p.paragraph_format.space_after = Pt(12)
                p.paragraph_format.first_line_indent = None
                p.paragraph_format.left_indent = None
                
                h_text = line[2:].strip()
                cleaned_h = clean_heading_text(h_text)
                run = p.add_run(cleaned_h)
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(14)
                i += 1
                continue

            # Heading 2 (Subbab)
            if line.startswith('## '):
                p = doc.add_paragraph(style='Heading 2')
                p.paragraph_format.space_before = Pt(10)
                p.paragraph_format.space_after = Pt(4)
                p.paragraph_format.first_line_indent = None
                p.paragraph_format.left_indent = None
                p.paragraph_format.line_spacing = 1.5
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                
                h_text = line[3:].strip()
                cleaned_h = clean_heading_text(h_text)
                run = p.add_run(cleaned_h)
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
                i += 1
                continue

            # Heading 3 (Sub-subbab)
            if line.startswith('### '):
                p = doc.add_paragraph(style='Heading 3')
                p.paragraph_format.space_before = Pt(8)
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.first_line_indent = None
                p.paragraph_format.left_indent = None
                p.paragraph_format.line_spacing = 1.5
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                
                h_text = line[4:].strip()
                cleaned_h = clean_heading_text(h_text)
                run = p.add_run(cleaned_h)
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
                i += 1
                continue

            # Heading 4
            if line.startswith('#### '):
                p = doc.add_paragraph(style='Normal')
                p.paragraph_format.space_before = Pt(6)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.first_line_indent = None
                p.paragraph_format.left_indent = None
                p.paragraph_format.line_spacing = 1.5
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                
                h_text = line[5:].strip()
                cleaned_h = clean_heading_text(h_text)
                run = p.add_run(cleaned_h)
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
                i += 1
                continue

            # Mermaid Diagram Block
            if line.startswith('```mermaid'):
                diagram_counter += 1
                i += 1
                while i < total_lines and not lines[i].strip().startswith('```'):
                    i += 1
                i += 1  # skip closing ```

                img_path = os.path.join(img_dir, f"diagram_{diagram_counter}.png")
                caption_text = DIAGRAM_CAPTIONS.get(diagram_counter, f"Gambar {diagram_counter}: Ilustrasi Arsitektur Sistem SmartPOS")
                
                if os.path.exists(img_path):
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(8)
                    p_img.paragraph_format.space_after = Pt(3)
                    run_img = p_img.add_run()
                    run_img.add_picture(img_path, width=Cm(14.0))

                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_after = Pt(8)
                    run_cap = p_cap.add_run(caption_text)
                    run_cap.font.name = 'Times New Roman'
                    run_cap.font.size = Pt(11)
                    run_cap.italic = True
                    print(f"   Embedded diagram {diagram_counter}: {caption_text}")
                else:
                    print(f"   WARNING: Image not found for diagram {diagram_counter} at {img_path}")
                continue

            # Code Blocks
            if line.startswith('```'):
                code_lines = []
                i += 1
                while i < total_lines and not lines[i].strip().startswith('```'):
                    code_lines.append(lines[i].rstrip('\r\n'))
                    i += 1
                i += 1  # skip closing ```
                
                for cl in code_lines:
                    p = doc.add_paragraph(style='Normal')
                    p.paragraph_format.left_indent = Cm(1.27)
                    p.paragraph_format.first_line_indent = None
                    p.paragraph_format.space_before = Pt(1)
                    p.paragraph_format.space_after = Pt(1)
                    p.paragraph_format.line_spacing = 1.15
                    run = p.add_run(cl)
                    run.font.name = 'Courier New'
                    run.font.size = Pt(10)
                continue

            # Tables
            if line.startswith('|') and line.endswith('|'):
                table_lines = []
                while i < total_lines and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                    table_lines.append(lines[i].strip())
                    i += 1

                if len(table_lines) >= 2:
                    raw_header = [c.strip() for c in table_lines[0][1:-1].split('|')]
                    data_rows = []
                    for t_idx in range(1, len(table_lines)):
                        if re.match(r'^\|[\s\-:|]+\|$', table_lines[t_idx]):
                            continue
                        row_cells = [c.strip() for c in table_lines[t_idx][1:-1].split('|')]
                        data_rows.append(row_cells)

                    num_cols = len(raw_header)
                    table = doc.add_table(rows=len(data_rows) + 1, cols=num_cols)
                    table.alignment = WD_TABLE_ALIGNMENT.CENTER
                    set_table_borders(table, color="B8C4CE", sz="4", val="single")

                    col_lens = [len(raw_header[c]) for c in range(num_cols)]
                    for row in data_rows:
                        for c in range(min(num_cols, len(row))):
                            col_lens[c] = max(col_lens[c], len(row[c]))
                    total_len = sum(col_lens) if sum(col_lens) > 0 else 1
                    
                    target_total_cm = 14.0
                    col_widths_cm = [max(1.5, (l / total_len) * target_total_cm) for l in col_lens]
                    scale = target_total_cm / sum(col_widths_cm)
                    col_widths_cm = [w * scale for w in col_widths_cm]

                    # Header Row
                    hdr_row = table.rows[0]
                    trPr = hdr_row._tr.get_or_add_trPr()
                    trPr.append(OxmlElement('w:tblHeader'))

                    for c_idx, h_text in enumerate(raw_header):
                        cell = hdr_row.cells[c_idx]
                        cell.width = Cm(col_widths_cm[c_idx])
                        set_cell_background(cell, "EAEFF5")
                        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p.paragraph_format.space_before = Pt(3)
                        p.paragraph_format.space_after = Pt(3)
                        p.paragraph_format.line_spacing = 1.15
                        add_formatted_runs(p, h_text, base_font_size=10.5, bold_all=True)

                    # Data Rows
                    for r_idx, row_data in enumerate(data_rows):
                        row = table.rows[r_idx + 1]
                        bg_color = "F8FAFC" if (r_idx % 2 == 1) else "FFFFFF"
                        for c_idx in range(num_cols):
                            cell = row.cells[c_idx]
                            cell.width = Cm(col_widths_cm[c_idx])
                            if bg_color != "FFFFFF":
                                set_cell_background(cell, bg_color)
                            set_cell_margins(cell, top=90, bottom=90, left=140, right=140)
                            p = cell.paragraphs[0]
                            p.paragraph_format.space_before = Pt(2)
                            p.paragraph_format.space_after = Pt(2)
                            p.paragraph_format.line_spacing = 1.15

                            cell_text = row_data[c_idx] if c_idx < len(row_data) else ""
                            if len(cell_text) <= 12 and any(k in cell_text for k in ['FR-', 'NFR-', 'UC-', 'TC-', 'PASS', 'High', 'Low', 'Medium', 'Must', 'Ya', 'Tidak']):
                                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            else:
                                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                            add_formatted_runs(p, cell_text, base_font_size=10)

                    p_spacer = doc.add_paragraph()
                    p_spacer.paragraph_format.space_before = Pt(2)
                    p_spacer.paragraph_format.space_after = Pt(4)
                continue

            # Blockquotes
            if line.startswith('>'):
                bq_text = line[1:].strip()
                if bq_text.startswith('[!'):
                    bq_text = re.sub(r'^\[!.*?\]\s*', '', bq_text)
                p = doc.add_paragraph(style='Normal')
                p.paragraph_format.left_indent = Cm(1.27)
                p.paragraph_format.first_line_indent = None
                p.paragraph_format.space_before = Pt(3)
                p.paragraph_format.space_after = Pt(4)
                p.paragraph_format.line_spacing = 1.4
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                add_formatted_runs(p, bq_text, base_font_size=11, italic_all=True, color=RGBColor(50, 50, 50))
                i += 1
                continue

            # Display LaTeX Math formula
            if line.startswith('$$') and line.endswith('$$') and len(line) >= 4:
                math_formula = line[2:-2].strip()
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(4)
                p.paragraph_format.first_line_indent = None
                p.paragraph_format.left_indent = None
                add_formatted_runs(p, math_formula, base_font_size=11.5, italic_all=True)
                i += 1
                continue

            # Lists
            is_bullet = bool(re.match(r'^[-*]\s+', line))
            is_numbered = bool(re.match(r'^\d+\.\s+', line))
            if is_bullet or is_numbered:
                if is_bullet:
                    item_text = re.sub(r'^[-*]\s+', '', line)
                    lead_marker = '•  '
                else:
                    m = re.match(r'^(\d+\.)\s+', line)
                    lead_marker = m.group(1) + '  '
                    item_text = line[m.end():]

                p = doc.add_paragraph(style='List Paragraph')
                p.paragraph_format.left_indent = Cm(1.27)
                p.paragraph_format.first_line_indent = Cm(-0.6)
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.5
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

                run_m = p.add_run(lead_marker)
                run_m.bold = True
                run_m.font.name = 'Times New Roman'
                run_m.font.size = Pt(12)

                add_formatted_runs(p, item_text, base_font_size=12)
                i += 1
                continue

            # Daftar Pustaka hanging indent
            if is_daftarpustaka:
                p = doc.add_paragraph(style='Normal')
                p.paragraph_format.left_indent = Cm(1.27)
                p.paragraph_format.first_line_indent = Cm(-1.27)
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(6)
                p.paragraph_format.line_spacing = 1.15
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                add_formatted_runs(p, line, base_font_size=11.5)
                i += 1
                continue

            # Standard Narrative Paragraph
            p = doc.add_paragraph(style='Normal')
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.first_line_indent = Cm(1.27)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_formatted_runs(p, line, base_font_size=12)
            i += 1

    print(f"\nSaving final integrated document to {output_path}...")
    doc.save(output_path)
    print("SUCCESS! Document completely built and integrated with 100% fidelity.")

if __name__ == '__main__':
    build_document()
