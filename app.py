from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.pichau.com.br/monitores/monitores-gamer') 
titulos = driver.find_elements(By.XPATH, "//h2[@class='MuiTypography-root jss78 jss79 MuiTypography-h6']")
precos = driver.find_elements(By.XPATH, "//div[@class='jss81']")

planilha = openpyxl.Workbook()
planilha.create_sheet("produtos")
produtos_sheet = planilha['produtos']
produtos_sheet['A1'].value = "Produto"
produtos_sheet['B1'].value = "Preço"


for titulo, preco in zip(titulos, precos):
    produtos_sheet.append([titulo.text,preco.text])

planilha.save("produtos.xlsx")