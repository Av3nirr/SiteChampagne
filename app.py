# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for
import mariadb
import datetime
import market

db = mariadb.connect(
    host="45.140.165.235",
    user="28594-database",
    password="-xMl6zU;G#Yv",
    database="28594-database"
)


# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/bouteilles', methods =["GET", "POST"])
def bouteilles():
    text = " "
    if request.method == "POST":
        # getting input with name = fname in HTML form
        brut = request.form.get("bnum")
        if brut == "":
            text = "Vous n'avez pas spécifié le nombre de brut"
            return render_template("bouteilles.html", result=text)
        rose = request.form.get("rnum")
        millesime = request.form.get("mnum")
        paiement = request.form.get("paiement")
        prix = request.form.get("prix")
        if rose == "":
            text = "Vous n'avez pas spécifié le nombre de rosé"
            return render_template("bouteilles.html", result=text)
        elif millesime == "":
            text = "Vous n'avez pas spécifié le nombre de millésime"
            return render_template("bouteilles.html", result=text)
        elif paiement == "":
            text = "Vous n'avez pas spécifié le mode de paiement"
            return render_template("bouteilles.html", result=text)
        elif prix == "":
            text = "Vous n'avez pas spécifié le prix"
            return render_template("bouteilles.html", result=text)
        heure = datetime.datetime.now()
        date = datetime.date.today()
        try:
            with db.cursor() as c:
                c.execute(f"insert into `bouteilles`(`brut`, `rose`, `millesime`, `paiement`, `prix`, `heure`, `date`) values ('{brut}','{rose}','{millesime}','{paiement}','{prix}','{heure}', '{str(date)}')")
                db.commit()
        except:
            print("Une erreur est survenue lors de la connection à la base de donnés !")


        text = f"Commande éffectuée, le client à commandé {brut} brut(s), {rose} Rosé(s) et {millesime} Millésime(s).\nLe client à réglé {prix}€ en {paiement}."
    return render_template("bouteilles.html", result=text)

#coupes
@app.route('/coupes', methods =["GET", "POST"])
def coupes():
    text = " "
    if request.method == "POST":
        # getting input with name = fname in HTML form
        brut = request.form.get("bnum")
        if brut == "":
            text = "Vous n'avez pas spécifié le nombre de brut"
            return render_template("coupes.html", result=text)
        rose = request.form.get("rnum")
        millesime = request.form.get("mnum")
        paiement = request.form.get("paiement")
        prix = request.form.get("prix")
        if rose == "":
            text = "Vous n'avez pas spécifié le nombre de rosé"
            return render_template("coupes.html", result=text)
        elif millesime == "":
            text = "Vous n'avez pas spécifié le nombre de millésime"
            return render_template("coupes.html", result=text)
        elif paiement == "":
            text = "Vous n'avez pas spécifié le mode de paiement"
            return render_template("coupes.html", result=text)
        elif prix == "":
            text = "Vous n'avez pas spécifié le prix"
            return render_template("coupes.html", result=text)
        heure = datetime.datetime.now()
        date = datetime.date.today()
        try:
            with db.cursor() as c:
                c.execute(f"insert into `coupes`(`brut`, `rose`, `millesime`, `paiement`, `prix`, `heure`, `date`) values ('{brut}','{rose}','{millesime}','{paiement}','{prix}','{heure}', '{str(date)}')")
                db.commit()
        except:
            print("Une erreur est survenue lors de la connection à la base de donnés !")


        text = f"Commande éffectuée, le client à commandé {brut} brut(s), {rose} Rosé(s) et {millesime} Millésime(s).\nLe client à réglé {prix}€ en {paiement}."
    return render_template("coupes.html", result=text)

@app.route('/bilan', methods =["GET", "POST"])
def bilan():
    result = ""
    ventes = []
    if request.method == "POST":
        date = request.form.get("date")
        print(date)
        with db.cursor() as c:
            c.execute("SELECT brut, rose, millesime, prix, paiement FROM bouteilles WHERE date = ?", (date,))
            for vente in c.fetchall():
                print(f"Vente: {vente}")
                ventes.append(vente)
            #bruts
            c.execute("SELECT brut FROM bouteilles WHERE date = ? AND paiement = ?", (date, "esp",))
            bruts_esp = 0
            for brut in c.fetchall():
                bruts_esp = bruts_esp+int(str(brut).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de bruts en Espèces: {bruts_esp}")
            c.execute("SELECT brut FROM bouteilles WHERE date = ? AND paiement = ?", (date, "cb",))
            bruts_cb = 0
            for brut in c.fetchall():
                bruts_cb = bruts_cb+int(str(brut).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de bruts en Carte Bancaire: {bruts_cb}")
            c.execute("SELECT brut FROM bouteilles WHERE date = ? AND paiement = ?", (date, "chq",))
            bruts_chq = 0
            for brut in c.fetchall():
                bruts_chq = bruts_chq+int(str(brut).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de bruts en Chèques: {bruts_chq}")
            #rose
            c.execute("SELECT rose FROM bouteilles WHERE date = ? AND paiement = ?", (date, "esp",))
            rose_esp = 0
            for rose in c.fetchall():
                rose_esp = rose_esp+int(str(rose).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de rosés en Espèces: {rose_esp}")
            c.execute("SELECT rose FROM bouteilles WHERE date = ? AND paiement = ?", (date, "cb",))
            rose_cb = 0
            for rose in c.fetchall():
                rose_cb = rose_cb+int(str(rose).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de rosés en Carte Bancaire: {rose_cb}")
            c.execute("SELECT rose FROM bouteilles WHERE date = ? AND paiement = ?", (date, "chq",))
            rose_chq = 0
            for rose in c.fetchall():
                rose_chq = rose_chq+int(str(rose).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de rosés en Chèques: {rose_chq}")
            #millesime
            c.execute("SELECT millesime FROM bouteilles WHERE date = ? AND paiement = ?", (date, "esp",))
            millesime_esp = 0
            for millesime in c.fetchall():
                millesime_esp = millesime_esp+int(str(millesime).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de Millésimes en Espèces: {millesime_esp}")
            c.execute("SELECT millesime FROM bouteilles WHERE date = ? AND paiement = ?", (date, "cb",))
            millesime_cb = 0
            for millesime in c.fetchall():
                millesime_cb = millesime_cb+int(str(millesime).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de Millésimes en Carte Bancaire: {millesime_cb}")
            c.execute("SELECT millesime FROM bouteilles WHERE date = ? AND paiement = ?", (date, "chq",))
            millesime_chq = 0
            for millesime in c.fetchall():
                millesime_chq = millesime_chq+int(str(millesime).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de Millésimes en Chèques: {millesime_chq}")
            #coupes brut cb
            c.execute("SELECT brut FROM coupes WHERE date = ? AND paiement = ?", (date, "cb",))
            coupes_b_cb = 0
            for brut in c.fetchall():
                coupes_b_cb = coupes_b_cb+int(str(brut).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de coupes bruts en Carte Bancaire: {coupes_b_cb}")
            #coupes brut esp
            c.execute("SELECT brut FROM coupes WHERE date = ? AND paiement = ?", (date, "esp",))
            coupes_b_esp = 0
            for brut in c.fetchall():
                coupes_b_esp = coupes_b_esp+int(str(brut).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de coupes bruts en Espèces: {coupes_b_esp}")
            #coupes rose cb
            c.execute("SELECT rose FROM coupes WHERE date = ? AND paiement = ?", (date, "cb",))
            coupes_r_cb = 0
            for rose in c.fetchall():
                coupes_r_cb = coupes_r_cb+int(str(rose).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de coupes rosé en Carte Bancaire: {coupes_r_cb}")
            #coupes rose esp
            c.execute("SELECT rose FROM coupes WHERE date = ? AND paiement = ?", (date, "esp",))
            coupes_r_esp = 0
            for rose in c.fetchall():
                coupes_r_esp = coupes_r_esp+int(str(rose).replace("(", "").replace(")", "").replace(",", ""))
            print(f"Nombre de coupes rosé en Espèces: {coupes_r_esp}")
            #total prix coupes
            c.execute("SELECT prix FROM coupes WHERE date = ? AND paiement = ?", (date, "cb"))
            coupes_cb = 0
            for prix in c.fetchall():
                prix_formatted = str(prix).replace("(", "").replace(")", "").replace(",", "")
                coupes_cb = coupes_cb+ float(prix_formatted)
                print(f"Total coupes carte bancaire: {coupes_cb}")
            c.execute("SELECT prix FROM coupes WHERE date = ? AND paiement = ?", (date, "esp"))
            coupes_esp = 0
            for prix in c.fetchall():
                prix_formatted = str(prix).replace("(", "").replace(")", "").replace(",", "")
                coupes_esp = coupes_esp+ float(prix_formatted)
                print(f"Total coupes espèces {coupes_esp}")
            #total prix
            c.execute("SELECT prix FROM bouteilles WHERE date = ? AND paiement = ?", (date, "cb"))
            cb = 0
            for prix in c.fetchall():
                prix_formatted = str(prix).replace("(", "").replace(")", "").replace(",", "")
                cb = cb+ float(prix_formatted)
                print(f"Total bouteilles cb: {cb}")
            c.execute("SELECT prix FROM bouteilles WHERE date = ? AND paiement = ?", (date, "esp"))
            esp = 0
            for prix in c.fetchall():
                prix_formatted = str(prix).replace("(", "").replace(")", "").replace(",", "")
                esp = esp+ float(prix_formatted)
                print(f"Total bouteilles Escpèces: {esp}")
            c.execute("SELECT prix FROM bouteilles WHERE date = ? AND paiement = ?", (date, "chq"))
            chq = 0
            for prix in c.fetchall():
                prix_formatted = str(prix).replace("(", "").replace(")", "").replace(",", "")
                chq = chq+ float(prix_formatted)
                print(f"Total bouteilles Chèques: {chq}")
            result = market.bilan(bruts_cb=bruts_cb, bruts_esp=bruts_esp, bruts_chq=bruts_chq, rose_cb=rose_cb, rose_esp=rose_esp, rose_chq=rose_chq, millesime_cb=millesime_cb, millesime_chq=millesime_chq, millesime_esp=millesime_esp, ccb=coupes_cb, cesp=coupes_esp, total_cb=cb, total_chq=chq, total_esp=esp, date=datetime.date.today())
    return render_template('bilan.html', result=result)

@app.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)