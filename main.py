from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CCP - Extrait de compte</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f4f6f8;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .header-top {
            background-color: #0d3b66;
            color: white;
            padding: 12px 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .logo-area {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logo-circle {
            background: white;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #0d3b66;
            font-size: 14px;
            text-align: center;
            line-height: 1.1;
        }
        .ccp-number {
            font-size: 18px;
            letter-spacing: 1px;
        }
        .menu-icon {
            font-size: 24px;
            color: #f4d03f;
            cursor: pointer;
        }
        .sub-header {
            background-color: #0d3b66;
            padding: 10px 15px 20px 15px;
            border-bottom: 4px solid #f4d03f;
        }
        .sub-header h2 {
            color: #f4d03f;
            font-size: 20px;
            margin: 0;
            font-weight: 500;
        }
        .container {
            padding: 15px;
            max-width: 600px;
            margin: auto;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .card-line {
            margin-bottom: 12px;
            font-size: 16px;
        }
        .card-line strong {
            color: #2c3e50;
        }
        .solde-title {
            color: #0d3b66;
            font-weight: bold;
            font-size: 18px;
            margin-top: 15px;
            margin-bottom: 8px;
        }
        .solde-badge {
            background-color: #0d3b66;
            color: white;
            display: inline-block;
            padding: 10px 18px;
            border-radius: 8px;
            font-size: 22px;
            font-weight: bold;
            letter-spacing: 0.5px;
        }
        .operations-title {
            font-size: 20px;
            color: #333;
            margin-bottom: 15px;
            font-weight: 400;
        }
        .divider {
            border: none;
            border-top: 1.5px solid #0d3b66;
            margin-bottom: 15px;
        }
        .date-section {
            font-weight: bold;
            color: #444;
            margin-bottom: 10px;
        }
        .operation-card {
            background: white;
            border-radius: 12px;
            padding: 15px 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 15px;
        }
        .op-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        .op-amount {
            color: #8b0000;
            font-weight: bold;
            font-size: 17px;
        }
        .op-tax {
            color: #555;
            font-size: 14px;
        }
        .op-details {
            display: flex;
            justify-content: space-between;
            color: #555;
            font-size: 15px;
            margin-bottom: 12px;
        }
        .op-solde-line {
            font-weight: bold;
            color: #222;
            font-size: 15px;
        }
        .footer-url {
            text-align: center;
            font-size: 13px;
            color: #0d3b66;
            margin-top: 30px;
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <div class="header-top">
        <div class="logo-area">
            <div class="logo-circle">Algérie<br>Poste</div>
            <span class="ccp-number">CCP 0029013970</span>
        </div>
        <div class="menu-icon">&#9776;</div>
    </div>

    <div class="sub-header">
        <h2>EXTRAIT DE COMPTE</h2>
    </div>

    <div class="container">
        <div class="card">
            <div class="card-line"><strong>Compte :</strong> 29013970</div>
            <div class="card-line"><strong>Date :</strong> 10/10/2026 à 16:47</div>
            <div class="solde-title">Votre solde :</div>
            <div class="solde-badge">310657,88 DA</div>
        </div>

        <div class="operations-title">Opérations récentes</div>
        <hr class="divider">

        <div class="date-section">07/10/2026 :</div>

        <div class="operation-card">
            <div class="op-header">
                <span class="op-amount">-10,00 DA</span>
                <span class="op-tax">Taxe : 0,00</span>
            </div>
            <div class="op-details">
                <span>205 TAXE</span>
                <span>Compte : 1515</span>
            </div>
            <div class="op-solde-line">
                Solde : 310657,88 DA
            </div>
        </div>

        <div class="footer-url">
            Politique de protection des données
        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
