from pystyle import *
from os import *
from time import *
import openpyxl
import shutil


def write(case, content):
    workbook = openpyxl.load_workbook(filename=f"./exports/{market_name}.xlsx")
    sheet = workbook["recap"]
    sheet[case] = content
    workbook.save(filename=f"./exports/{market_name}.xlsx")


def bilan(bruts_cb, bruts_esp, bruts_chq, rose_cb, rose_esp, rose_chq, millesime_cb, millesime_esp, millesime_chq, cesp, ccb, total_cb, total_esp, total_chq, date):
    global market_name
    market_name = f"marche_{date}"
    workbook = openpyxl.load_workbook(filename="template_marchés.xlsx")
    sheet = workbook["recap"]
    sheet["A1"] = market_name
    workbook.save(filename=f"./exports/{market_name}.xlsx")
    #brut
    write("B5", bruts_cb)
    write("B6", bruts_esp)
    write("B7", bruts_chq)
    #prestige
    write("C5", millesime_cb)
    write("C6", millesime_esp)
    write("C7", millesime_chq)
    #rose
    write("D5", rose_cb)
    write("D6", rose_esp)
    write("D7", rose_chq)
    #totaux
    write("F5", total_cb)
    write("F6", total_esp)
    write("F7", total_chq)
    #coupes rose
    write("F9", ccb)
    #coupes brut
    write("F10", cesp)
    return f"Aucune erreur, le fichier à été enregistré dans {market_name}.xlsx"