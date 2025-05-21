# app.py
from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('certificado_form.html')

@app.route('/gerar_certificado', methods=['POST'])
def gerar_certificado():
    nome = request.form['nome']
    curso = request.form['curso']
    carga_horaria = request.form['carga_horaria']
    data = request.form['data']
    logo_url = os.path.join(os.getcwd(), 'static', 'logo.png')
    print("logo_url:", logo_url)

    rendered = render_template('certificado_pdf.html',
                                nome=nome,
                                curso=curso,
                                carga_horaria=carga_horaria,
                                data=data,
                                logo_url=logo_url)

    pdf_path = f'certificado_{nome.replace(" ", "_")}.pdf'
    pdfkit.from_string(rendered, pdf_path, options={'enable-local-file-access': ''})

    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    

