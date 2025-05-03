
from flask import Flask, request
from flask_mail import Mail, Message
from fpdf import FPDF
import io

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='es7555397@gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='es7555397@gmail.com',
    MAIL_PASSWORD='SENHA_DO_APP'
)

mail = Mail(app)

@app.route("/enviar", methods=["POST"])
def enviar():
    data = request.get_json()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Formulário CAT - Comunicação de Acidente de Trabalho", ln=True)
    pdf.ln(5)
    for key, value in data.items():
        pdf.multi_cell(0, 10, txt=f"{key.replace('_', ' ').capitalize()}: {value}")
    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    msg = Message("Nova CAT Recebida", sender="SEU_EMAIL@gmail.com", recipients=["es7555397@gmail.com"])
    msg.body = "Segue em anexo a CAT preenchida."
    msg.attach("cat.pdf", "application/pdf", buffer.read())

    mail.send(msg)
    return "CAT enviada com sucesso!"
