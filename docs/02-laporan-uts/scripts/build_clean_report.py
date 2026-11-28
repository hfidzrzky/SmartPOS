import os
import re
import docx
from docx.shared import Cm, Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="CCCCCC", sz="4", val="single"):
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

def disable_auto_num(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    for child in list(pPr):
        if child.tag.endswith('numPr'):
            pPr.remove(child)
    numPr = OxmlElement('w:numPr')
    ilvl = OxmlElement('w:ilvl')
    ilvl.set(qn('w:val'), '0')
    numId = OxmlElement('w:numId')
    numId.set(qn('w:val'), '0')
    numPr.append(ilvl)
    numPr.append(numId)
    pPr.append(numPr)

def clean_math_text(text):
    clean = text.replace(r'\text{', '').replace('}', '')
    clean = clean.replace(r'\approx', '≈')
    clean = clean.replace(r'\le', '≤').replace(r'\ge', '≥').replace(r'\pm', '±')
    clean = clean.replace(r'\Delta', 'Δ').replace(r'\times', '×').replace(r'\sum', 'Σ')
    clean = clean.replace(r'\frac', '').replace(r'\quad', ' ')
    clean = clean.replace(r'\textbf{', '').replace(r'\rightarrow', '→').replace(r'\leftrightarrow', '↔')
    clean = clean.replace('$\\rightarrow$', '→').replace('$\\leftrightarrow$', '↔')
    clean = clean.replace('$\\le$', '≤').replace('$\\ge$', '≥')
    clean = clean.replace('$->$', '→').replace('$<-$', '←')
    return clean

def add_formatted_runs(paragraph, text, base_font_size=12, italic_all=False, color=None):
    pattern = r'(\*\*.*?\*\*|\*.*?\*|`.*?`|\$.*?\$)'
    parts = re.split(pattern, text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**') and len(part) >= 4:
            run = paragraph.add_run(clean_math_text(part[2:-2]))
            run.bold = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            if italic_all:
                run.italic = True
            run.font.color.rgb = color if color else RGBColor(0, 0, 0)
        elif part.startswith('*') and part.endswith('*') and len(part) >= 2:
            run = paragraph.add_run(clean_math_text(part[1:-1]))
            run.italic = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            run.font.color.rgb = color if color else RGBColor(0, 0, 0)
        elif part.startswith('`') and part.endswith('`') and len(part) >= 2:
            run = paragraph.add_run(part[1:-1])
            run.font.name = 'Consolas'
            run.font.size = Pt(base_font_size - 1)
            run.font.color.rgb = RGBColor(0x1F, 0x24, 0x2E)
            if italic_all:
                run.italic = True
        elif part.startswith('$') and part.endswith('$') and len(part) >= 2:
            clean_math = clean_math_text(part[1:-1])
            run = paragraph.add_run(clean_math)
            run.italic = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            run.font.color.rgb = color if color else RGBColor(0, 0, 0)
        else:
            clean_text = clean_math_text(part)
            run = paragraph.add_run(clean_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            if italic_all:
                run.italic = True
            run.font.color.rgb = color if color else RGBColor(0, 0, 0)

def get_table_col_widths(headers, num_cols):
    joined_header = ' '.join(headers).lower()
    if 'model proses sdlc' in joined_header:
        return [2.8, 2.7, 2.5, 2.7, 3.3]
    elif 'kategori' in joined_header and 'stakeholder' in joined_header:
        return [1.3, 2.2, 2.8, 3.9, 3.8]
    elif 'masalah nyata lapangan' in joined_header:
        return [1.0, 4.3, 4.3, 4.4]
    elif 'modul & fungsi' in joined_header and 'kasir' in joined_header:
        return [3.5, 2.0, 2.2, 6.3]
    elif 'id kebutuhan' in joined_header and 'domain modul' in joined_header:
        return [2.0, 3.0, 9.0]
    elif 'id nfr' in joined_header:
        return [1.8, 2.7, 5.0, 4.5]
    elif 'high priority' in joined_header:
        return [2.4, 2.9, 2.9, 2.9, 2.9]
    elif 'target user story' in joined_header or 'requirements traceability' in joined_header:
        # Table 8 RTM: 7 columns
        return [1.6, 1.8, 1.8, 2.5, 2.7, 2.0, 1.6]
    elif 'nama atribut' in joined_header:
        # Kamus Data (6 columns)
        return [2.4, 3.4, 1.8, 2.0, 2.4, 2.0]
    elif 'terpetakan pada use case' in joined_header:
        # FR vs UC (5 columns)
        return [1.6, 4.5, 2.5, 3.8, 1.6]
    elif 'context diagram' in joined_header and 'dfd level 0' in joined_header:
        # Context vs DFD (4 columns)
        return [2.5, 4.5, 4.5, 2.5]
    elif 'spesifikasi pada induk' in joined_header:
        # DFD Balancing (4 columns)
        return [3.0, 4.0, 4.2, 2.8]
    elif 'skenario prosedur pengujian' in joined_header:
        # Black Box Testing (6 columns)
        return [1.5, 1.5, 4.3, 3.7, 1.5, 1.5]
    else:
        w = 14.0 / num_cols
        return [w] * num_cols

def populate_clean_report():
    # Always read template from clean backup
    template_docx = r'd:\Projects\SmartPOS\docs\LAPORAN_UTS_TEMPLATE_BASE.docx'
    master_md = r'd:\Projects\SmartPOS\docs\02-laporan-uts\LAPORAN_UTUH_UTS_SMARTPOS.md'
    img_dir = r'd:\Projects\SmartPOS\docs\02-laporan-uts\diagram_images'
    output_docx = r'd:\Projects\SmartPOS\docs\LAPORAN UTS KELOMPOK 5 - SMARTPOS SISTEM KASIR DAN MANAJEMEN USAHA BERBASIS DESKTOP OFFLINE-FIRST - SOFTWARE REQUIREMENTS SPECIFICATION (SRS).docx'

    # If base template doesn't exist yet, make a copy of the clean structure
    if not os.path.exists(template_docx):
        import shutil
        shutil.copy(output_docx, template_docx)

    print("Opening template document...")
    doc = docx.Document(template_docx)

    # Verify margins
    sec = doc.sections[0]
    sec.left_margin = Cm(4.0)
    sec.top_margin = Cm(3.0)
    sec.right_margin = Cm(3.0)
    sec.bottom_margin = Cm(3.0)

    # Format KATA PENGANTAR (P15)
    p15 = doc.paragraphs[15]
    p15.alignment = WD_ALIGN_PARAGRAPH.CENTER
    disable_auto_num(p15)
    if p15.runs:
        p15.runs[0].font.name = 'Times New Roman'
        p15.runs[0].font.size = Pt(14)
        p15.runs[0].bold = True
        p15.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    # Find DAFTAR ISI in the original template
    p_di_idx = -1
    for idx, p in enumerate(doc.paragraphs):
        if p.text.strip() == 'DAFTAR ISI':
            p_di_idx = idx
            break

    print(f"DAFTAR ISI found at paragraph index {p_di_idx}...")

    # Format DAFTAR ISI paragraph
    p_di = doc.paragraphs[p_di_idx]
    p_di.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_di.paragraph_format.page_break_before = True
    disable_auto_num(p_di)
    if p_di.runs:
        p_di.runs[0].font.name = 'Times New Roman'
        p_di.runs[0].font.size = Pt(14)
        p_di.runs[0].bold = True
        p_di.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    # Prune any empty paragraphs between KATA PENGANTAR end (P33) and DAFTAR ISI (P36)
    for p in doc.paragraphs[34:p_di_idx]:
        if not p.text.strip() or p.text == '\n':
            p._p.getparent().remove(p._p)

    # Re-find DAFTAR ISI index after removal
    p_di_idx = -1
    for idx, p in enumerate(doc.paragraphs):
        if p.text.strip() == 'DAFTAR ISI':
            p_di_idx = idx
            break

    paras_to_remove = doc.paragraphs[p_di_idx + 1:]
    for p in paras_to_remove:
        p._p.getparent().remove(p._p)

    print("Populating DAFTAR ISI entries...")
    toc_items = [
        ("KATA PENGANTAR", True, 0),
        ("DAFTAR ISI", True, 0),
        ("BAB I: PENDAHULUAN", True, 0),
        ("1.1 Latar Belakang", False, 1),
        ("1.2 Identifikasi Masalah", False, 1),
        ("1.3 Rumusan Masalah", False, 1),
        ("1.4 Tujuan Pengembangan Sistem", False, 1),
        ("1.5 Batasan Masalah", False, 1),
        ("1.6 Gambaran Umum Sistem", False, 1),
        ("1.7 Pemilihan Model Proses Pengembangan Perangkat Lunak", False, 1),
        ("BAB II: SOFTWARE REQUIREMENTS SPECIFICATION (SRS)", True, 0),
        ("2.1 Deskripsi Umum Sistem", False, 1),
        ("2.2 Identifikasi Stakeholder", False, 1),
        ("2.3 Teknik Elisitasi Kebutuhan", False, 1),
        ("2.4 Identifikasi Aktor dan Hak Akses", False, 1),
        ("2.5 Kebutuhan Fungsional (Functional Requirements)", False, 1),
        ("2.6 Kebutuhan Nonfungsional (Nonfunctional Requirements)", False, 1),
        ("2.7 User Story", False, 1),
        ("2.8 Acceptance Criteria", False, 1),
        ("2.9 Prioritas Kebutuhan", False, 1),
        ("2.10 Requirements Traceability Matrix (RTM)", False, 1),
        ("BAB III: PEMODELAN ANALISIS SISTEM", True, 0),
        ("3.1 Use Case Diagram (Standar OMG UML 2.5.1)", False, 1),
        ("3.2 Deskripsi / Skenario Use Case", False, 1),
        ("3.3 Activity Diagram", False, 1),
        ("3.4 Context Diagram (Notasi Aliran Data)", False, 1),
        ("3.5 Data Flow Diagram (DFD) Level 0", False, 1),
        ("3.6 Data Flow Diagram (DFD) Level 1 (Dekomposisi & Uji Balancing)", False, 1),
        ("3.7 Kamus Data (Data Dictionary)", False, 1),
        ("BAB IV: ANALISIS DAN EVALUASI HASIL PEMODELAN", True, 0),
        ("4.1 Kesesuaian Kebutuhan Fungsional dengan Use Case Diagram", False, 1),
        ("4.2 Konsistensi Use Case dan Activity Diagram", False, 1),
        ("4.3 Konsistensi Context Diagram dan DFD Level 0", False, 1),
        ("4.4 Konsistensi DFD Level 0 dan DFD Level 1 (Pemeriksaan Balancing)", False, 1),
        ("4.5 Evaluasi Keterlacakan Kebutuhan (Traceability Analysis)", False, 1),
        ("4.6 Kesimpulan Analisis dan Evaluasi Sistem", False, 1),
        ("DAFTAR PUSTAKA", True, 0),
        ("LAMPIRAN: MATRIKS PENGUJIAN BLACK-BOX SISTEM (TC-01 s.d. TC-20)", True, 0)
    ]

    for title, is_bold, level in toc_items:
        p_toc = doc.add_paragraph()
        p_toc.paragraph_format.line_spacing = 1.15
        if level == 0:
            p_toc.paragraph_format.space_before = Pt(4)
            p_toc.paragraph_format.space_after = Pt(2)
            p_toc.paragraph_format.left_indent = Cm(0)
        else:
            p_toc.paragraph_format.space_before = Pt(1.5)
            p_toc.paragraph_format.space_after = Pt(1.5)
            p_toc.paragraph_format.left_indent = Cm(0.7)

        run = p_toc.add_run(title)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.bold = is_bold
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Page break after DAFTAR ISI to begin BAB I
    doc.add_page_break()

    # Read master markdown
    print(f"Reading master content from {master_md}...")
    with open(master_md, 'r', encoding='utf-8') as f:
        md_lines = f.readlines()

    # Find line where BAB I starts
    start_line_idx = -1
    for idx, line in enumerate(md_lines):
        if line.strip().startswith('# BAB I:'):
            start_line_idx = idx
            break

    if start_line_idx == -1:
        raise ValueError("Could not find '# BAB I:' in master markdown!")

    content_lines = md_lines[start_line_idx:]
    print(f"Processing {len(content_lines)} content lines from BAB I to end...")

    i = 0
    n = len(content_lines)
    in_code_block = False
    code_block_lines = []
    is_mermaid = False
    mermaid_counter = 0
    just_added_page_break = True

    while i < n:
        raw_line = content_lines[i]
        line = raw_line.strip()

        # Handle page breaks
        if line == r'\newpage':
            if not just_added_page_break:
                doc.add_page_break()
                just_added_page_break = True
            i += 1
            continue

        # Handle horizontal divider
        if line == '---':
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run('━' * 55)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            just_added_page_break = False
            i += 1
            continue

        # Handle Code blocks & Mermaid
        if line.startswith('```'):
            if not in_code_block:
                in_code_block = True
                is_mermaid = 'mermaid' in line
                code_block_lines = []
            else:
                in_code_block = False
                if is_mermaid:
                    mermaid_counter += 1
                    img_path = os.path.join(img_dir, f'diag_{mermaid_counter}.png')
                    if os.path.exists(img_path) and os.path.getsize(img_path) > 1000:
                        print(f"  Embedding Mermaid Diagram {mermaid_counter:02d} ({os.path.basename(img_path)})...")
                        p_img = doc.add_paragraph()
                        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_img.paragraph_format.space_before = Pt(8)
                        p_img.paragraph_format.space_after = Pt(6)
                        run = p_img.add_run()
                        run.add_picture(img_path, width=Cm(13.8))
                        just_added_page_break = False
                    else:
                        print(f"  Fallback text for diagram {mermaid_counter}...")
                        p_fallback = doc.add_paragraph()
                        p_fallback.paragraph_format.space_before = Pt(4)
                        p_fallback.paragraph_format.space_after = Pt(4)
                        p_fallback.paragraph_format.left_indent = Cm(0.5)
                        run = p_fallback.add_run('\n'.join(code_block_lines))
                        run.font.name = 'Consolas'
                        run.font.size = Pt(9.5)
                        run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
                        just_added_page_break = False
                else:
                    code_text = '\n'.join(code_block_lines)
                    table = doc.add_table(rows=1, cols=1)
                    table.alignment = WD_TABLE_ALIGNMENT.CENTER
                    cell = table.cell(0, 0)
                    cell.width = Cm(14.0)
                    set_cell_background(cell, "F5F6F8")
                    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
                    set_table_borders(table, color="D0D5DD")
                    p_cell = cell.paragraphs[0]
                    p_cell.paragraph_format.space_before = Pt(3)
                    p_cell.paragraph_format.space_after = Pt(3)
                    run = p_cell.add_run(code_text)
                    run.font.name = 'Consolas'
                    run.font.size = Pt(9.5)
                    run.font.color.rgb = RGBColor(0x1F, 0x24, 0x2E)
                    p_spacer = doc.add_paragraph()
                    p_spacer.paragraph_format.space_before = Pt(0)
                    p_spacer.paragraph_format.space_after = Pt(4)
                    just_added_page_break = False
            i += 1
            continue

        if in_code_block:
            code_block_lines.append(raw_line.rstrip('\r\n'))
            i += 1
            continue

        # Handle Tables
        if line.startswith('|') and line.endswith('|'):
            table_lines = []
            while i < n and content_lines[i].strip().startswith('|') and content_lines[i].strip().endswith('|'):
                table_lines.append(content_lines[i].strip())
                i += 1

            rows_data = []
            for t_line in table_lines:
                if re.match(r'^\|[\s\:\-]+(\Auto-increment|[\s\:\-\|]+)$', t_line) or '---' in t_line:
                    continue
                cleaned_line = t_line.replace(r'\|', '___ESCAPED_PIPE___')
                raw_cells = [c.strip() for c in cleaned_line.split('|')[1:-1]]
                cells = [c.replace('___ESCAPED_PIPE___', '|') for c in raw_cells]
                if cells:
                    rows_data.append(cells)

            if rows_data:
                num_cols = max(len(r) for r in rows_data)
                col_widths = get_table_col_widths(rows_data[0], num_cols)

                table = doc.add_table(rows=len(rows_data), cols=num_cols)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                set_table_borders(table, color="CCCCCC")

                is_dense_table = num_cols >= 6 or 'traceability' in ' '.join(rows_data[0]).lower()
                tbl_font_size = 8.5 if (num_cols >= 7 or is_dense_table) else 9.5
                tbl_hdr_size = 9.0 if (num_cols >= 7 or is_dense_table) else 10.0

                for r_idx, row in enumerate(rows_data):
                    table_row = table.rows[r_idx]
                    trPr = table_row._tr.get_or_add_trPr()
                    trPr.append(OxmlElement('w:cantSplit'))

                    is_header = (r_idx == 0)
                    if is_header:
                        trPr.append(OxmlElement('w:tblHeader'))

                    for c_idx in range(num_cols):
                        cell = table_row.cells[c_idx]
                        col_w = col_widths[c_idx] if c_idx < len(col_widths) else (14.0 / num_cols)
                        cell.width = Cm(col_w)
                        cell_text = row[c_idx] if c_idx < len(row) else ''

                        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
                        if is_header:
                            set_cell_background(cell, "EAEFF5")
                        else:
                            if r_idx % 2 == 1:
                                set_cell_background(cell, "FAFBFC")
                            else:
                                set_cell_background(cell, "FFFFFF")

                        p_cell = cell.paragraphs[0]
                        p_cell.paragraph_format.space_before = Pt(2)
                        p_cell.paragraph_format.space_after = Pt(2)
                        p_cell.paragraph_format.line_spacing = 1.15

                        short_tokens = ['pass', 'fail', 'high', 'medium', 'low', 'fr-', 'uc-', 'nfr-', 'tc-', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']
                        is_short = len(cell_text) <= 10 or any(tok in cell_text.lower() for tok in short_tokens)

                        if is_header or (is_short and not any(k in cell_text.lower() for k in ['deskripsi', 'rumusan', 'prosedur', 'analisis'])):
                            p_cell.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        else:
                            p_cell.alignment = WD_ALIGN_PARAGRAPH.LEFT

                        add_formatted_runs(p_cell, cell_text, base_font_size=tbl_hdr_size if is_header else tbl_font_size, italic_all=False)
                        if is_header:
                            for run in p_cell.runs:
                                run.bold = True

                p_after_table = doc.add_paragraph()
                p_after_table.paragraph_format.space_before = Pt(0)
                p_after_table.paragraph_format.space_after = Pt(4)
                just_added_page_break = False
            continue

        if not line:
            i += 1
            continue

        # Handle Headings
        # Level 1: Major Chapters (BAB, DAFTAR PUSTAKA, LAMPIRAN) -> 14 pt bold, center
        if line.startswith('# ') and not line.startswith('## '):
            heading_text = clean_math_text(line[2:].strip().replace('**', '').replace('*', ''))
            if not just_added_page_break:
                doc.add_page_break()

            p = doc.add_paragraph()
            p.style = doc.styles['Heading 1']
            disable_auto_num(p)
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(heading_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(14)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            just_added_page_break = False
            i += 1
            continue

        # Level 2: Sub-chapters (e.g. 1.1 Latar Belakang) -> 12 pt bold, left
        if line.startswith('## ') and not line.startswith('### '):
            heading_text = clean_math_text(line[3:].strip().replace('**', '').replace('*', ''))
            p = doc.add_paragraph()
            p.style = doc.styles['Heading 2']
            disable_auto_num(p)
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(heading_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            just_added_page_break = False
            i += 1
            continue

        # Level 3: Sub-sub-chapters (e.g. 1.7.1 Analisis Komparatif...) -> 12 pt bold, left
        if line.startswith('### ') and not line.startswith('#### '):
            heading_text = clean_math_text(line[4:].strip().replace('**', '').replace('*', ''))
            p = doc.add_paragraph()
            p.style = doc.styles['Heading 3']
            disable_auto_num(p)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(heading_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            just_added_page_break = False
            i += 1
            continue

        # Level 4: Deep subheadings -> 12 pt bold, left
        if line.startswith('#### '):
            heading_text = clean_math_text(line[5:].strip().replace('**', '').replace('*', ''))
            p = doc.add_paragraph()
            p.style = doc.styles['Heading 4']
            disable_auto_num(p)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(heading_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            just_added_page_break = False
            i += 1
            continue

        # Blockquote / Notes -> 12 pt italic, line spacing 1.3
        if line.startswith('>'):
            quote_text = line[1:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.8)
            p.paragraph_format.right_indent = Cm(0.5)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.3
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_formatted_runs(p, quote_text, base_font_size=12, italic_all=True)
            just_added_page_break = False
            i += 1
            continue

        # Bullet and Numbered Lists -> 12 pt, line spacing 1.4
        list_match = re.match(r'^(\-|\*|\d+\.)\s+(.*)', line)
        if list_match:
            bullet_type = list_match.group(1)
            item_text = list_match.group(2)
            p = doc.add_paragraph()
            p.style = doc.styles['List Paragraph'] if 'List Paragraph' in doc.styles else doc.styles['Normal']
            p.paragraph_format.left_indent = Cm(0.7)
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(2.5)
            p.paragraph_format.line_spacing = 1.4
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            
            if bullet_type in ['-', '*']:
                run_b = p.add_run('•  ')
                run_b.bold = True
            else:
                run_b = p.add_run(bullet_type + '  ')
                run_b.bold = True
            run_b.font.name = 'Times New Roman'
            run_b.font.size = Pt(12)
            run_b.font.color.rgb = RGBColor(0, 0, 0)

            add_formatted_runs(p, item_text, base_font_size=12)
            just_added_page_break = False
            i += 1
            continue

        # Standard Body Paragraph -> 12 pt Times New Roman, line spacing 1.5, Justified
        p = doc.add_paragraph()
        p.style = doc.styles['Normal']
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.5
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_formatted_runs(p, line, base_font_size=12)
        just_added_page_break = False
        i += 1

    print(f"Saving final populated document to {output_docx}...")
    doc.save(output_docx)
    print("SUCCESS! Document successfully populated and saved.")

if __name__ == '__main__':
    populate_clean_report()
