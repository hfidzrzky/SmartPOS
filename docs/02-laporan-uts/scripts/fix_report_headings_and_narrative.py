import docx
import re
import os
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def clean_heading_text(text):
    # Remove leading numbering like "1.7.2 ", "2.1 ", "3.2.1 ", etc.
    cleaned = re.sub(r'^(\d+(\.\d+)+\s+)', '', text.strip())
    # Remove single numbers if any like "2. "
    cleaned = re.sub(r'^(\d+\.\s+)', '', cleaned)
    # Clean latex math symbols
    cleaned = cleaned.replace('$→$', '→').replace('$\\rightarrow$', '→')
    cleaned = cleaned.replace('$↔$', '↔').replace('$\\leftrightarrow$', '↔').replace('$≤ftrightarrow$', '↔')
    cleaned = cleaned.replace('**', '').replace('*', '')
    return cleaned

def fix_document():
    source_path = r'docs/LAPORAN UTS KELOMPOK 5 - SMARTPOS SISTEM KASIR DAN MANAJEMEN USAHA BERBASIS DESKTOP OFFLINE-FIRST - SOFTWARE REQUIREMENTS SPECIFICATION (SRS).docx'
    revised_path = r'docs/LAPORAN UTS KELOMPOK 5 - SMARTPOS SISTEM KASIR DAN MANAJEMEN USAHA BERBASIS DESKTOP OFFLINE-FIRST - SOFTWARE REQUIREMENTS SPECIFICATION (SRS)_REVISED.docx'
    
    print(f"Loading document from {source_path}...")
    doc = docx.Document(source_path)

    # 1. Strip duplicate leading numbers from Headings (Heading 2, Heading 3, Heading 4)
    # Word's multi-level list will automatically supply the numbers correctly!
    for i, p in enumerate(doc.paragraphs):
        if p.style.name.startswith('Heading 2') or p.style.name.startswith('Heading 3') or p.style.name.startswith('Heading 4'):
            old_text = p.text
            new_text = clean_heading_text(old_text)
            if new_text != old_text:
                p.text = ''
                run = p.add_run(new_text)
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
                run.bold = True
                run.font.color.rgb = RGBColor(0, 0, 0)

    # 2. Fix narrative in Section 1.7
    for i, p in enumerate(doc.paragraphs):
        # Fix 1.7.1 intro
        if 'evaluasi komparatif terhadap enam model proses perangkat lunak mengacu pada materi perkuliahan Pertemuan 2' in p.text:
            p.text = (
                "Untuk menentukan model proses yang paling efektif dalam pengembangan perangkat lunak SmartPOS, "
                "dilakukan evaluasi komparatif terhadap enam paradigma model proses rekayasa perangkat lunak "
                "(Software Development Life Cycle / SDLC). Evaluasi ini didasarkan pada parameter karakteristik kebutuhan sistem, "
                "toleransi risiko kegagalan transaksi, pola pengiriman perangkat lunak (delivery cadence), "
                "serta kesesuaian operasional terhadap unit usaha toko sembako dan pangkalan gas LPG fisik:"
            )
            p.paragraph_format.line_spacing = 1.5
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)
                r.font.color.rgb = RGBColor(0, 0, 0)

        # Fix 1.7.2 narrative
        if 'Mengacu pada ketentuan perkuliahan Pertemuan 2 Slide 22' in p.text:
            p.text = (
                "Berdasarkan hasil analisis komparatif terhadap karakteristik operasional dan kebutuhan unit usaha di lapangan, "
                "tim rekayasa perangkat lunak menetapkan justifikasi metodologis pemilihan model proses secara formal dan argumentatif sebagai berikut:"
            )
            p.paragraph_format.line_spacing = 1.5
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)
                r.font.color.rgb = RGBColor(0, 0, 0)

        # Fix ### Pernyataan Pemilihan Model Proses:
        if '### Pernyataan Pemilihan Model Proses' in p.text or 'Pernyataan Pemilihan Model Proses' in p.text:
            p.text = "Pernyataan Keputusan Pemilihan Model Proses Rekayasa Sistem:"
            p.paragraph_format.line_spacing = 1.5
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)
                r.bold = True
                r.font.color.rgb = RGBColor(0, 0, 0)

        # Fix 1.7.2 quote block
        if 'Kami memilih model *Iterative-Incremental' in p.text or 'Kami memilih model Iterative-Incremental' in p.text:
            p.text = (
                "“Kami memilih model Iterative-Incremental dengan pendekatan Agile-Kanban karena karakteristik proyek SmartPOS "
                "menuntut arsitektur inti kasir yang dapat diuji coba dan divalidasi terlebih dahulu secara mandiri oleh pengguna "
                "(kasir dan pemilik toko), sementara modul logika yang kompleks (seperti penatausahaan sirkulasi tabung gas LPG "
                "dan rekalkulasi HPP rata-rata tertimbang) dikembangkan, diuji, dan diintegrasikan secara bertahap tanpa "
                "mengganggu fungsi operasional kasir yang telah berjalan stabil.”"
            )
            p.paragraph_format.line_spacing = 1.5
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)
                r.italic = True
                r.font.color.rgb = RGBColor(0, 0, 0)

        # Fix Section 2.2 stakeholder intro
        if 'Berdasarkan materi perkuliahan Pertemuan 3' in p.text:
            p.text = (
                "Dalam rekayasa kebutuhan perangkat lunak, identifikasi pemangku kepentingan (stakeholders) "
                "dilakukan secara menyeluruh guna memetakan seluruh pihak yang berinteraksi langsung maupun tidak langsung dengan sistem. "
                "Pemangku kepentingan dikelompokkan ke dalam tiga kategori hierarki:"
            )
            p.paragraph_format.line_spacing = 1.5
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)
                r.font.color.rgb = RGBColor(0, 0, 0)

        # Fix Daftar Pustaka item 10
        if 'Slide Bahan Perkuliahan Rekayasa Perangkat Lunak' in p.text:
            p.text = (
                "10. Bramantio, D. R. (2026). Bahan Ajar Perkuliahan Rekayasa Perangkat Lunak: "
                "Kerangka Kerja SDLC, Spesifikasi Kebutuhan, dan Pemodelan Analisis Sistem. "
                "Bandung: Departemen Teknik Informatika, Fakultas Industri Kreatif, Universitas Teknologi Bandung."
            )
            p.paragraph_format.line_spacing = 1.5
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)
                r.font.color.rgb = RGBColor(0, 0, 0)

    # Save to revised file
    print(f"Saving revised document to {revised_path}...")
    doc.save(revised_path)
    print("Document successfully saved to revised path!")

    # Try saving to original file as well
    try:
        doc.save(source_path)
        print(f"SUCCESS: Also overwritten original file at {source_path}!")
    except Exception as e:
        print(f"Notice: Original file {source_path} is currently locked by Word: {e}")
        print("Once Word is closed, the revised file can overwrite the original.")

if __name__ == '__main__':
    fix_document()
