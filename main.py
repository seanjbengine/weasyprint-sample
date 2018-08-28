from weasyprint import HTML, CSS

HTML('base.html').write_pdf('resume.pdf', stylesheets=[CSS('style.css')])
