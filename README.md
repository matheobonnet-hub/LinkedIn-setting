# BYS Setting Agent — Revenew

Assistant IA pour les setters BYS qui prospectent sur LinkedIn pour Mathéo Bonnet.

**Campagne active :** Revenew (plateforme SaaS outbound)
**Objectif :** RDV 20 min ou questionnaire Tally — jamais pitcher

---

## Ce que fait l'agent

| Onglet | Utilisation |
|--------|-------------|
| ✉️ Icebreaker | Génère un premier message personnalisé à partir des infos du prospect |
| 💬 Conversation | Coache sur la réponse à envoyer dans une conversation en cours |
| 🔄 Relance | Génère une relance sans mentionner le silence (max 2 relances) |
| ❓ Coach | Répond à toutes questions sur la méthodologie, l'angle Revenew, les objections |

---

## Déploiement rapide

### Option 1 — Streamlit Community Cloud (recommandé)

1. Fork ce repo sur votre compte GitHub
2. Aller sur [share.streamlit.io](https://share.streamlit.io)
3. Connecter le repo, sélectionner `app.py`
4. Dans **Secrets**, ajouter :
   ```
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
5. Déployer — lien partageable avec tous les setters

### Option 2 — Lancement local

```bash
git clone https://github.com/matheobonnet-hub/LinkedIn-setting.git
cd LinkedIn-setting

pip install -r requirements.txt

cp .env.example .env
# Éditer .env et ajouter votre clé API Anthropic

streamlit run app.py
```

L'app s'ouvre sur `http://localhost:8501`

---

## Configuration

La clé API Anthropic peut être configurée de 3 façons :
1. **Variable d'environnement** : `ANTHROPIC_API_KEY` dans `.env`
2. **Secrets Streamlit** : via le panneau de déploiement Streamlit Cloud
3. **Interface** : directement dans la barre latérale de l'app (pour les tests)

---

## Liens essentiels

- 📅 Agenda Mathéo : https://cal.com/matheo.bonnet/consultative-meeting
- 📋 Questionnaire Revenew : https://tally.so/r/44EbKk
- 🌐 Revenew : https://revenew.tech/
- 🏢 BYS : https://buildyoursales.tech/en
