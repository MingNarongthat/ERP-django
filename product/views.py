from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import View
from io import StringIO
from django.template.loader import get_template
from django.template import Context
from cgi import escape
from datetime import datetime
from PIL import Image, ImageDraw, ImageFilter
from django.db import models
from .models import AllCustomer, Image
from django.core.files.storage import FileSystemStorage
# Returns a datetime object containing the local date and time
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus.flowables import Image
from reportlab.platypus.tables import Table, TableStyle, GRID_STYLE, BOX_STYLE, LABELED_GRID_STYLE, COLORED_GRID_STYLE, LIST_STYLE, LongTable
from reportlab.rl_config import TTFSearchPath
import os

dateTimeObj = datetime.now()

def Document(request):
	return render(request, 'product/Document.html')

def Document2(request):
	return render(request, 'product/Document2.html')

def newProduct(request):
	return render(request, 'product/newProduct.html')


def GENPDF(request):
	width, height = A4
	daystart = datetime.now().strftime('%d-%m-%Y')
	dayend = datetime.now().strftime('%d-%m-%Y')
	dateTimeObj = datetime.now()
	Quo_no = str(dateTimeObj.year) + str(dateTimeObj.month) + str(dateTimeObj.day) + str(dateTimeObj.hour+7) +str(dateTimeObj.minute) + str(dateTimeObj.second)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Quo-{}.pdf"'.format(Quo_no)# re
	p = canvas.Canvas(response, pagesize=A4)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	TTFSearchPath.append(str(BASE_DIR) + '/product')
	pdfmetrics.registerFont(TTFont('supermarket', "supermarket.ttf"))
	# pdfmetrics.registerFont(TTFont('supermarket', 'supermarket.woff'))
	styleSheet = getSampleStyleSheet()
	styleN = styleSheet["Normal"]
	styleT = styleSheet["Title"]
	styleT.alignment = 0 # center 1, right 2

	
	firm = request.POST["firmname"]
	address1 = request.POST["address"]
	address2 = request.POST["address2"]
	address = address1 + ' ' +  address2
	province1 = request.POST["province"]
	zipcode = request.POST["zipcode"]
	province = province1 + ' ' +  zipcode
	tax = request.POST["tax"]
	tel1 = request.POST["tel1"]
	# tel2 = request.POST["tel2"]
	productID = request.POST["productID"]

	link_logo = 'https://www.c2premium.com/wp-content/uploads/2019/09/website-03-03.png'
	link_image1 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_1.jpg'
	link_image2 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_2.jpg'
	link_image3 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_3.jpg'
	link_image4 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_4.jpg'
	link_image5 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_5.jpg'
	link_image6 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_draft_1.jpg'

	name_Product = request.POST["nameProduct"]
	amount = int(request.POST["amount"])
	price = int(request.POST["price"])
	Total_price = round(int(request.POST["amount"])*int(request.POST["price"]),2)
	Total_tax = round(int(request.POST["amount"])*int(request.POST["price"])*1.07,2)
	Vat = round(int(request.POST["amount"])*int(request.POST["price"])*0.07,2)
	
	# p.drawImage("https://drive.google.com/file/d/1IyG_Wpl4b8shMO3349uRcH9PeDhx45SU/view", 75, 240 * mm, width=30)
	### ==========> ผู้เสนอ ===================================================================
	ptext = Paragraph("<font size=28 name='supermarket' color='darkblue'>ใบเสนอราคา/QUOTATION</font>".format(Quo_no), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 280 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ผู้เสนอ</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 265 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 265 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>18/1-2 พระรามหกตัดใหม่ซอย 4 ถนนพระรามหกตัดใหม่</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 260 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>แขวงรองเมือง เขตปทุมวัน กรุงเทพฯ 10330</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 255 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>เลขประจำตัวผู้เสียภาษี: 0105562135191</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 250 *mm)

	p.line(38 *mm, 246 *mm, 95 *mm, 246 *mm) # line

	### ==========> ผู้ซื้อ ===================================================================
	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ผู้ซื้อ</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 243 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(firm), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 243 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(address), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 238 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(province), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 233 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>เลขประจำตัวผู้เสียภาษี: {}</font>".format(tax), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 228 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>โทร: {}</font>".format(tel1), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 223 *mm)

	### ==========> วันเวลา เลขใบ ===================================================================
	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>DATE</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 285 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>QUOTATION NO.</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 280 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>USER NO.</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 275 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>{}</font>".format(datetime.now().strftime('%d-%m-%Y')), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 285 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>{}</font>".format(Quo_no), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 280 *mm)

	# ptext = Paragraph("<font size=11 name='supermarket'>{}</font>".format(Quo_no), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 170 *mm, 275 *mm)

	### ==========> ราคา ===================================================================
	ptext = Paragraph("<font size=28 name='supermarket' color='red'>THB</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 250 *mm)

	ptext = Paragraph("<font size=28 name='supermarket' color='red'>{:,}</font>".format(Total_tax), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 163 *mm, 250 *mm)

	### ==========> ราคา ===================================================================
	p.line(20 *mm, 220 *mm, 190 *mm, 220 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>No.</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 30 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>DESCRIPTION</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 77 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>QTY.</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 133 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>PRICE</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 150 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>TOTAL</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 210 *mm)

	p.line(20 *mm, 210 *mm, 190 *mm, 210 *mm)

	### ==========> สินค้า 1 ===================================================================
	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>1</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 30 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(name_Product), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(amount), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 133 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 150 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Total_price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 195 *mm)

	### ==========> สินค้า 2 ===================================================================
	# ptext = Paragraph("<font size=12 name='supermarket'>{}</font>".format(request.POST(NO2)), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 30 *mm, 195 *mm)

	# ptext = Paragraph("<font size=12 name='supermarket'>{}</font>".format(name_Product2), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 77 *mm, 195 *mm)

	# ptext = Paragraph("<font size=12 name='supermarket'>{}</font>".format(amount2), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 133 *mm, 195 *mm)

	# ptext = Paragraph("<font size=12 name='supermarket'>{:,}</font>".format(price2), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 150 *mm, 195 *mm)

	# ptext = Paragraph("<font size=12 name='supermarket'>{:,}</font>".format(Total_price), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 170 *mm, 195 *mm)

	### ==========> ข้อมูลฝั่งลูกค้า ===================================================================
	p.line(20 *mm, 90 *mm, 190 *mm, 90 *mm)

	ptext = Paragraph("<font size=8 name='supermarket'>*ราคานี้รวมค่าจัดส่งแล้ว	กำหนดส่ง: 30-35 วันนับจากวันที่ยืนยันแบบสินค้า</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 85 *mm) 

	p.line(20 *mm, 80 *mm, 110 *mm, 80 *mm) # x top
	p.line(20 *mm, 55 *mm, 110 *mm, 55 *mm) # x bottom
	p.line(20 *mm, 55 *mm, 20 *mm, 80 *mm) # x left
	p.line(110 *mm, 55 *mm, 110 *mm, 80 *mm) # x right

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>โอนเข้าบัญชี:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 75 *mm)	

	ptext = Paragraph("<font size=10 name='supermarket' color='red'>ธนาคาร ออมสิน สาขาสำนักพหลโยธิน เงินฝากเผื่อเรียก</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 75 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='red'>020-3-0161656-9 บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 70 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>Email:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 65 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>phannarong@c2tradinggroup.com</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 65 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>Tel:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 60 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>094-296-3261 (โอ่ง)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 60 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>ในนาม {}</font>".format(firm), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 50 *mm)

	### ==========> ข้อมูลฝั่งลผู้ขาย ===================================================================
	p.line(120 *mm, 80 *mm, 190 *mm, 80 *mm) # x top

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ยอดรวมสินค้า</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Total_price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>Vat 7%</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 70 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 70 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Vat), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 70 *mm)

	p.line(120 *mm, 67.5 *mm, 190 *mm, 67.5 *mm) # x middle

	ptext = Paragraph("<font size=18 name='supermarket' color='red'>รวมทั้งสิ้น</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 62.5*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='red'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 62.5*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='red'>{:,}</font>".format(Total_tax), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 62.5*mm)

	p.line(120 *mm, 55 *mm, 190 *mm, 55 *mm) # x bottom

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>ในนาม บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 50 *mm)

	### ==========> ลายเซน ===================================================================
	p.line(20 *mm, 25 *mm, 55 *mm, 25 *mm)
	p.line(60 *mm, 25 *mm, 95 *mm, 25 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color= 'darkblue'>{}</font>".format(datetime.now().strftime('%d-%m-%Y')), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 168 *mm, 27 *mm)
	p.line(125 *mm, 25 *mm, 160 *mm, 25 *mm)
	p.line(165 *mm, 25 *mm, 190 *mm, 25 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>(</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 20 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 55 *mm, 20 *mm)

	p.drawImage("https://gdurl.com/e6F8", 128 *mm, 26 * mm, width=70,height=50)
	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>(พันธุ์ณรงค์	ศรีนะภาพรรณ)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 126.5 *mm, 20 *mm)

	p.showPage()
	### ==========> Next Page ==========================================================================================
	### ==========> Next Page ==========================================================================================
	ptext = Paragraph("<font size=16 name='supermarket' color='red'>{}</font>".format(productID), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 265 *mm)

	p.drawImage(link_logo, 135 *mm, 270 * mm, width=50 *mm,height=10*mm,)

	p.drawImage(link_image1, 25 * mm, 160 * mm, width=105 * mm, height=105 * mm)
	p.drawImage(link_image2, 135 *mm, 215 * mm, width=50 *mm,height=50*mm,)
	p.drawImage(link_image3, 135 *mm, 160 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link_image4, 135 *mm, 105 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link_image5, 80 *mm, 105 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link_image6, 25 *mm, 105 * mm, width=50*mm,height=50*mm,)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>ราคา</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 90*mm)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>บาท</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 90 *mm, 90*mm)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>{:,}</font>".format(price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 60 *mm, 90*mm)

	ptext = Paragraph("<font size=14 name='supermarket' color='darkblue'>{}</font>".format(name_Product), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 75*mm)

	p.line(0 *mm, 20 *mm, 220 *mm, 20 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>สั่งซื้อ หรือ ติดต่อสอบถามข้อมูลเพิ่มเติม :</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 15 *mm, 15*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>TEL: 094-296-3261</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 80 *mm, 15*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>LINE@: c2premium (มี @ ด้านหน้าด้วย)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 120 *mm, 15*mm)

	p.save()

	return response

def GENPDF2(request):
	width, height = A4
	daystart = datetime.now().strftime('%d-%m-%Y')
	dayend = datetime.now().strftime('%d-%m-%Y')
	dateTimeObj = datetime.now()
	Quo_no = str(dateTimeObj.year) + str(dateTimeObj.month) + str(dateTimeObj.day) + str(dateTimeObj.hour+7) +str(dateTimeObj.minute) + str(dateTimeObj.second)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Quo-{}.pdf"'.format(Quo_no)# re
	p = canvas.Canvas(response, pagesize=A4)
	p = canvas.Canvas(response, pagesize=A4)

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	TTFSearchPath.append(str(BASE_DIR) + '/product')
	pdfmetrics.registerFont(TTFont('supermarket', 'supermarket.ttf'))
	# pdfmetrics.registerFont(TTFont('supermarket', 'supermarket.ttf'))

	styleSheet = getSampleStyleSheet()
	styleN = styleSheet["Normal"]
	styleT = styleSheet["Title"]
	styleT.alignment = 0 # center 1, right 2

	
	firm = request.POST["firmname"]
	address1 = request.POST["address"]
	address2 = request.POST["address2"]
	address = address1 + ' ' +  address2
	province1 = request.POST["province"]
	zipcode = request.POST["zipcode"]
	province = province1 + ' ' +  zipcode
	tax = request.POST["tax"]
	tel1 = request.POST["tel1"]
	# tel2 = request.POST["tel2"]
	productID = request.POST["productID"]
	productID2 = request.POST["productID2"]
	print(productID2)

	link_logo = 'https://www.c2premium.com/wp-content/uploads/2019/09/website-03-03.png'
	link_image1 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_1.jpg'
	link_image2 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_2.jpg'
	link_image3 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_3.jpg'
	link_image4 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_4.jpg'
	link_image5 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_pic_5.jpg'
	link_image6 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID + '_draft_1.jpg'

	link2_image1 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID2 + '_pic_1.jpg'
	link2_image2 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID2 + '_pic_2.jpg'
	link2_image3 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID2 + '_pic_3.jpg'
	link2_image4 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID2 + '_pic_4.jpg'
	link2_image5 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID2 + '_pic_5.jpg'
	link2_image6 = 'https://www.c2premium.com/wp-content/uploads/2020/06/' + productID2 + '_draft_1.jpg'

	name_Product = request.POST["nameProduct"]
	name_Product2 = request.POST["nameProduct2"]

	amount = int(request.POST["amount"])
	amount2 = int(request.POST["amount2"])

	price = int(request.POST["price"])
	price2 = int(request.POST["price2"])

	Total_price = round(int(request.POST["amount"])*int(request.POST["price"]),2)
	Total_price2 = round(int(request.POST["amount2"])*int(request.POST["price2"]),2)

	Total_tax = round(int(request.POST["amount"])*int(request.POST["price"])*1.07,2)
	Total_tax2 = round(int(request.POST["amount2"])*int(request.POST["price2"])*1.07,2)

	Vat = round(int(request.POST["amount"])*int(request.POST["price"])*0.07,2)
	Vat2 = round(int(request.POST["amount2"])*int(request.POST["price2"])*0.07,2)
	
	# p.drawImage("https://drive.google.com/file/d/1IyG_Wpl4b8shMO3349uRcH9PeDhx45SU/view", 75, 240 * mm, width=30)
	### ==========> ผู้เสนอ ===================================================================
	ptext = Paragraph("<font size=28 name='supermarket' color='darkblue'>ใบเสนอราคา/QUOTATION</font>".format(Quo_no), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 280 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ผู้เสนอ</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 265 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 265 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>18/1-2 พระรามหกตัดใหม่ซอย 4 ถนนพระรามหกตัดใหม่</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 260 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>แขวงรองเมือง เขตปทุมวัน กรุงเทพฯ 10330</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 255 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>เลขประจำตัวผู้เสียภาษี: 0105562135191</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 250 *mm)

	p.line(38 *mm, 246 *mm, 95 *mm, 246 *mm) # line

	### ==========> ผู้ซื้อ ===================================================================
	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ผู้ซื้อ</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 243 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(firm), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 243 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(address), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 238 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(province), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 233 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>เลขประจำตัวผู้เสียภาษี: {}</font>".format(tax), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 228 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>โทร: {}</font>".format(tel1), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 223 *mm)

	### ==========> วันเวลา เลขใบ ===================================================================
	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>DATE</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 285 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>QUOTATION NO.</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 280 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>USER NO.</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 275 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>{}</font>".format(datetime.now().strftime('%d-%m-%Y')), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 285 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>{}</font>".format(Quo_no), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 280 *mm)

	# ptext = Paragraph("<font size=11 name='supermarket'>{}</font>".format(Quo_no), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 170 *mm, 275 *mm)

	### ==========> ราคา ===================================================================
	ptext = Paragraph("<font size=28 name='supermarket' color='red'>THB</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 250 *mm)

	ptext = Paragraph("<font size=28 name='supermarket' color='red'>{:,}</font>".format(Total_tax+Total_tax2), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 163 *mm, 250 *mm)

	### ==========> ราคา ===================================================================
	p.line(20 *mm, 220 *mm, 190 *mm, 220 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>No.</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 30 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>DESCRIPTION</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 77 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>QTY.</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 133 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>PRICE</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 150 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>TOTAL</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 210 *mm)

	p.line(20 *mm, 210 *mm, 190 *mm, 210 *mm)

	### ==========> สินค้า 1 ===================================================================
	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>1</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 30 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(name_Product), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(amount), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 133 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 150 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Total_price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 195 *mm)

	### ==========> สินค้า 2 ===================================================================
	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>2</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 30 *mm, 185 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(name_Product2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 185 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(amount2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 133 *mm, 185 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(price2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 150 *mm, 185 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Total_price2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 185 *mm)

	### ==========> ข้อมูลฝั่งลูกค้า ===================================================================
	p.line(20 *mm, 90 *mm, 190 *mm, 90 *mm)

	ptext = Paragraph("<font size=8 name='supermarket'>*ราคานี้รวมค่าจัดส่งแล้ว	กำหนดส่ง: 30-35 วันนับจากวันที่ยืนยันแบบสินค้า</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 85 *mm) 

	p.line(20 *mm, 80 *mm, 110 *mm, 80 *mm) # x top
	p.line(20 *mm, 55 *mm, 110 *mm, 55 *mm) # x bottom
	p.line(20 *mm, 55 *mm, 20 *mm, 80 *mm) # x left
	p.line(110 *mm, 55 *mm, 110 *mm, 80 *mm) # x right

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>โอนเข้าบัญชี:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 75 *mm)	

	ptext = Paragraph("<font size=10 name='supermarket' color='red'>ธนาคาร ออมสิน สาขาสำนักพหลโยธิน เงินฝากเผื่อเรียก</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 75 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='red'>020-3-0161656-9 บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 70 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>Email:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 65 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>phannarong@c2tradinggroup.com</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 65 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>Tel:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 60 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>094-296-3261 (โอ่ง)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 60 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>ในนาม {}</font>".format(firm), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 50 *mm)

	### ==========> ข้อมูลฝั่งลผู้ขาย ===================================================================
	p.line(120 *mm, 80 *mm, 190 *mm, 80 *mm) # x top

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ยอดรวมสินค้า</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Total_price+Total_price2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>Vat 7%</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 70 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 70 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Vat+Vat2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 70 *mm)

	p.line(120 *mm, 67.5 *mm, 190 *mm, 67.5 *mm) # x middle

	ptext = Paragraph("<font size=18 name='supermarket' color='red'>รวมทั้งสิ้น</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 62.5*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='red'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 62.5*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='red'>{:,}</font>".format(Total_tax+Total_tax2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 62.5*mm)

	p.line(120 *mm, 55 *mm, 190 *mm, 55 *mm) # x bottom

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>ในนาม บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 50 *mm)

	### ==========> ลายเซน ===================================================================
	p.line(20 *mm, 25 *mm, 55 *mm, 25 *mm)
	p.line(60 *mm, 25 *mm, 95 *mm, 25 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(datetime.now().strftime('%d-%m-%Y')), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 168 *mm, 27 *mm)
	p.line(125 *mm, 25 *mm, 160 *mm, 25 *mm)
	p.line(165 *mm, 25 *mm, 190 *mm, 25 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>(</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 20 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 55 *mm, 20 *mm)

	p.drawImage("https://gdurl.com/e6F8", 128 *mm, 26 * mm, width=70,height=50)
	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>(พันธุ์ณรงค์	ศรีนะภาพรรณ)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 126.5 *mm, 20 *mm)

	p.showPage()
	### ==========> Next Page ==========================================================================================
	### ==========> Next Page ==========================================================================================
	ptext = Paragraph("<font size=16 name='supermarket' color='red'>{}</font>".format(productID), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 265 *mm)

	p.drawImage(link_logo, 135 *mm, 270 * mm, width=50 *mm,height=10*mm,)

	p.drawImage(link_image1, 25 * mm, 160 * mm, width=105 * mm, height=105 * mm)
	p.drawImage(link_image2, 135 *mm, 215 * mm, width=50 *mm,height=50*mm,)
	p.drawImage(link_image3, 135 *mm, 160 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link_image4, 135 *mm, 105 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link_image5, 80 *mm, 105 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link_image6, 25 *mm, 105 * mm, width=50*mm,height=50*mm,)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>ราคา</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 90*mm)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>บาท</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 90 *mm, 90*mm)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>{:,}</font>".format(price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 60 *mm, 90*mm)

	ptext = Paragraph("<font size=14 name='supermarket' color='darkblue'>{}</font>".format(name_Product), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 75*mm)

	p.line(0 *mm, 20 *mm, 220 *mm, 20 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>สั่งซื้อ หรือ ติดต่อสอบถามข้อมูลเพิ่มเติม :</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 15 *mm, 15*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>TEL: 094-296-3261</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 80 *mm, 15*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>LINE@: c2premium (มี @ ด้านหน้าด้วย)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 120 *mm, 15*mm)

	p.showPage()
	### ==========> Next Page ==========================================================================================
	### ==========> Next Page ==========================================================================================
	ptext = Paragraph("<font size=16 name='supermarket' color='red'>{}</font>".format(productID), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 265 *mm)

	p.drawImage(link_logo, 135 *mm, 270 * mm, width=50 *mm,height=10*mm,)

	p.drawImage(link2_image1, 25 * mm, 160 * mm, width=105 * mm, height=105 * mm)
	p.drawImage(link2_image2, 135 *mm, 215 * mm, width=50 *mm,height=50*mm,)
	p.drawImage(link2_image3, 135 *mm, 160 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link2_image4, 135 *mm, 105 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link2_image5, 80 *mm, 105 * mm, width=50*mm,height=50*mm,)
	p.drawImage(link2_image6, 25 *mm, 105 * mm, width=50*mm,height=50*mm,)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>ราคา</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 90*mm)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>บาท</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 90 *mm, 90*mm)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>{:,}</font>".format(price2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 60 *mm, 90*mm)

	ptext = Paragraph("<font size=14 name='supermarket' color='darkblue'>{}</font>".format(name_Product2), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 75*mm)

	p.line(0 *mm, 20 *mm, 220 *mm, 20 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>สั่งซื้อ หรือ ติดต่อสอบถามข้อมูลเพิ่มเติม :</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 15 *mm, 15*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>TEL: 094-296-3261</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 80 *mm, 15*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>LINE@: c2premium (มี @ ด้านหน้าด้วย)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 120 *mm, 15*mm)

	p.save()

	return response

def AddCustomer(request):
	if request.method == 'POST':
		data = request.POST.copy()
		customer_id = data.get('customer_id')
		tax_id = data.get('tax_id')
		company = data.get('company')
		customer_address = data.get('customer_address')
		customer_type = data.get('customer_type')

		new = AllCustomer()
		new.customer_id = customer_id
		new.tax_id = tax_id
		new.company = company
		new.customer_address = customer_address
		new.customer_type = customer_type
		new.save()
	return render(request,'product/addcustomer.html')

def ShowCustomer(request):
    customer_id = AllCustomer.objects.all() # pull data from database all
    context = {'customer_id':customer_id}
    return render(request,'product/Customer.html',context)

def GENPDF3(request):
	width, height = A4
	daystart = datetime.now().strftime('%d-%m-%Y')
	dayend = datetime.now().strftime('%d-%m-%Y')
	dateTimeObj = datetime.now()
	Quo_no = str(dateTimeObj.year) + str(dateTimeObj.month) + str(dateTimeObj.day) + str(dateTimeObj.hour+7) +str(dateTimeObj.minute) + str(dateTimeObj.second)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Quo-{}.pdf"'.format(Quo_no)# re
	p = canvas.Canvas(response, pagesize=A4)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	TTFSearchPath.append(str(BASE_DIR) + '/product')
	pdfmetrics.registerFont(TTFont('supermarket', "supermarket.ttf"))
	# pdfmetrics.registerFont(TTFont('supermarket', 'supermarket.woff'))
	styleSheet = getSampleStyleSheet()
	styleN = styleSheet["Normal"]
	styleT = styleSheet["Title"]
	styleT.alignment = 0 # center 1, right 2

	
	firm = request.POST["firmname"]
	address1 = request.POST["address"]
	address2 = request.POST["address2"]
	address = address1 + ' ' +  address2
	province1 = request.POST["province"]
	zipcode = request.POST["zipcode"]
	province = province1 + ' ' +  zipcode
	tax = request.POST["tax"]
	tel1 = request.POST["tel1"]
	# tel2 = request.POST["tel2"]
	productID = request.POST["productID"]

	link_logo = 'https://www.c2premium.com/wp-content/uploads/2019/09/website-03-03.png'
	
	link_image1 = request.FILES('img1')
	profile_obj=Image(profile_picture=image1).save()
	

	name_Product = request.POST["nameProduct"]
	amount = int(request.POST["amount"])
	price = int(request.POST["price"])
	Total_price = round(int(request.POST["amount"])*int(request.POST["price"]),2)
	Total_tax = round(int(request.POST["amount"])*int(request.POST["price"])*1.07,2)
	Vat = round(int(request.POST["amount"])*int(request.POST["price"])*0.07,2)
	
	# p.drawImage("https://drive.google.com/file/d/1IyG_Wpl4b8shMO3349uRcH9PeDhx45SU/view", 75, 240 * mm, width=30)
	### ==========> ผู้เสนอ ===================================================================
	ptext = Paragraph("<font size=28 name='supermarket' color='darkblue'>ใบเสนอราคา/QUOTATION</font>".format(Quo_no), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 280 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ผู้เสนอ</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 265 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 265 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>18/1-2 พระรามหกตัดใหม่ซอย 4 ถนนพระรามหกตัดใหม่</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 260 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>แขวงรองเมือง เขตปทุมวัน กรุงเทพฯ 10330</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 255 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>เลขประจำตัวผู้เสียภาษี: 0105562135191</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 250 *mm)

	p.line(38 *mm, 246 *mm, 95 *mm, 246 *mm) # line

	### ==========> ผู้ซื้อ ===================================================================
	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ผู้ซื้อ</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 243 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(firm), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 243 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(address), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 238 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(province), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 233 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>เลขประจำตัวผู้เสียภาษี: {}</font>".format(tax), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 228 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>โทร: {}</font>".format(tel1), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 223 *mm)

	### ==========> วันเวลา เลขใบ ===================================================================
	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>DATE</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 285 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>QUOTATION NO.</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 280 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>USER NO.</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 275 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>{}</font>".format(datetime.now().strftime('%d-%m-%Y')), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 285 *mm)

	ptext = Paragraph("<font size=11 name='supermarket' color='darkblue'>{}</font>".format(Quo_no), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 280 *mm)

	# ptext = Paragraph("<font size=11 name='supermarket'>{}</font>".format(Quo_no), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 170 *mm, 275 *mm)

	### ==========> ราคา ===================================================================
	ptext = Paragraph("<font size=28 name='supermarket' color='red'>THB</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 130 *mm, 250 *mm)

	ptext = Paragraph("<font size=28 name='supermarket' color='red'>{:,}</font>".format(Total_tax), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 163 *mm, 250 *mm)

	### ==========> ราคา ===================================================================
	p.line(20 *mm, 220 *mm, 190 *mm, 220 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>No.</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 30 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>DESCRIPTION</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 77 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>QTY.</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 133 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>PRICE</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 150 *mm, 210 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>TOTAL</font>", styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 210 *mm)

	p.line(20 *mm, 210 *mm, 190 *mm, 210 *mm)

	### ==========> สินค้า 1 ===================================================================
	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>1</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 30 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(name_Product), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 38 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{}</font>".format(amount), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 133 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 150 *mm, 195 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Total_price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 170 *mm, 195 *mm)

	### ==========> สินค้า 2 ===================================================================
	# ptext = Paragraph("<font size=12 name='supermarket'>{}</font>".format(request.POST(NO2)), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 30 *mm, 195 *mm)

	# ptext = Paragraph("<font size=12 name='supermarket'>{}</font>".format(name_Product2), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 77 *mm, 195 *mm)

	# ptext = Paragraph("<font size=12 name='supermarket'>{}</font>".format(amount2), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 133 *mm, 195 *mm)

	# ptext = Paragraph("<font size=12 name='supermarket'>{:,}</font>".format(price2), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 150 *mm, 195 *mm)

	# ptext = Paragraph("<font size=12 name='supermarket'>{:,}</font>".format(Total_price), styleN)
	# ptext.wrapOn(p, width, height)
	# ptext.drawOn(p, 170 *mm, 195 *mm)

	### ==========> ข้อมูลฝั่งลูกค้า ===================================================================
	p.line(20 *mm, 90 *mm, 190 *mm, 90 *mm)

	ptext = Paragraph("<font size=8 name='supermarket'>*ราคานี้รวมค่าจัดส่งแล้ว	กำหนดส่ง: 30-35 วันนับจากวันที่ยืนยันแบบสินค้า</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 85 *mm) 

	p.line(20 *mm, 80 *mm, 110 *mm, 80 *mm) # x top
	p.line(20 *mm, 55 *mm, 110 *mm, 55 *mm) # x bottom
	p.line(20 *mm, 55 *mm, 20 *mm, 80 *mm) # x left
	p.line(110 *mm, 55 *mm, 110 *mm, 80 *mm) # x right

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>โอนเข้าบัญชี:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 75 *mm)	

	ptext = Paragraph("<font size=10 name='supermarket' color='red'>ธนาคาร ออมสิน สาขาสำนักพหลโยธิน เงินฝากเผื่อเรียก</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 75 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='red'>020-3-0161656-9 บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 70 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>Email:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 65 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>phannarong@c2tradinggroup.com</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 65 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>Tel:</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 60 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>094-296-3261 (โอ่ง)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 40 *mm, 60 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>ในนาม {}</font>".format(firm), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 22 *mm, 50 *mm)

	### ==========> ข้อมูลฝั่งลผู้ขาย ===================================================================
	p.line(120 *mm, 80 *mm, 190 *mm, 80 *mm) # x top

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>ยอดรวมสินค้า</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Total_price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 75 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>Vat 7%</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 70 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 70 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>{:,}</font>".format(Vat), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 70 *mm)

	p.line(120 *mm, 67.5 *mm, 190 *mm, 67.5 *mm) # x middle

	ptext = Paragraph("<font size=18 name='supermarket' color='red'>รวมทั้งสิ้น</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 62.5*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='red'>THB</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 160 *mm, 62.5*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='red'>{:,}</font>".format(Total_tax), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 175 *mm, 62.5*mm)

	p.line(120 *mm, 55 *mm, 190 *mm, 55 *mm) # x bottom

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>ในนาม บริษัท ซีทูเทรดดิ้ง จำกัด</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 122 *mm, 50 *mm)

	### ==========> ลายเซน ===================================================================
	p.line(20 *mm, 25 *mm, 55 *mm, 25 *mm)
	p.line(60 *mm, 25 *mm, 95 *mm, 25 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color= 'darkblue'>{}</font>".format(datetime.now().strftime('%d-%m-%Y')), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 168 *mm, 27 *mm)
	p.line(125 *mm, 25 *mm, 160 *mm, 25 *mm)
	p.line(165 *mm, 25 *mm, 190 *mm, 25 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>(</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 20 *mm, 20 *mm)

	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 55 *mm, 20 *mm)

	p.drawImage("https://gdurl.com/e6F8", 128 *mm, 26 * mm, width=70,height=50)
	ptext = Paragraph("<font size=10 name='supermarket' color='darkblue'>(พันธุ์ณรงค์	ศรีนะภาพรรณ)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 126.5 *mm, 20 *mm)

	p.showPage()
	### ==========> Next Page ==========================================================================================
	### ==========> Next Page ==========================================================================================
	ptext = Paragraph("<font size=16 name='supermarket' color='red'>{}</font>".format(productID), styleT)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 265 *mm)

	p.drawImage(link_logo, 135 *mm, 270 * mm, width=50 *mm,height=10*mm,)

	p.drawImage(link_image1, 25 * mm, 160 * mm, width=105 * mm, height=105 * mm)
	# p.drawImage(link_image2, 135 *mm, 215 * mm, width=50 *mm,height=50*mm,)
	# p.drawImage(link_image3, 135 *mm, 160 * mm, width=50*mm,height=50*mm,)
	# p.drawImage(link_image4, 135 *mm, 105 * mm, width=50*mm,height=50*mm,)
	# p.drawImage(link_image5, 80 *mm, 105 * mm, width=50*mm,height=50*mm,)
	# p.drawImage(link_image6, 25 *mm, 105 * mm, width=50*mm,height=50*mm,)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>ราคา</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 90*mm)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>บาท</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 90 *mm, 90*mm)

	ptext = Paragraph("<font size=22 name='supermarket' color='red'>{:,}</font>".format(price), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 60 *mm, 90*mm)

	ptext = Paragraph("<font size=14 name='supermarket' color='darkblue'>{}</font>".format(name_Product), styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 25 *mm, 75*mm)

	p.line(0 *mm, 20 *mm, 220 *mm, 20 *mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>สั่งซื้อ หรือ ติดต่อสอบถามข้อมูลเพิ่มเติม :</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 15 *mm, 15*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>TEL: 094-296-3261</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 80 *mm, 15*mm)

	ptext = Paragraph("<font size=12 name='supermarket' color='darkblue'>LINE@: c2premium (มี @ ด้านหน้าด้วย)</font>", styleN)
	ptext.wrapOn(p, width, height)
	ptext.drawOn(p, 120 *mm, 15*mm)

	p.save()

	return response

 


