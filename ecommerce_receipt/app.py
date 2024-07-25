from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_receipt', methods=['POST'])
def generate_receipt():
    customer_name = request.form['customer_name']
    amount = request.form['amount']
    order_id = random.randint(1000, 9999)  # Generate a random order ID
    
    # Create a PDF file in memory
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    c.drawString(100, 750, f"Receipt for {customer_name}")
    c.drawString(100, 730, f"Amount: ${amount}")
    c.drawString(100, 710, f"Order ID: {order_id}")
    c.showPage()
    c.save()

    pdf_buffer.seek(0)
    
    return send_file(pdf_buffer, as_attachment=True, download_name=f'receipt_{order_id}.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
