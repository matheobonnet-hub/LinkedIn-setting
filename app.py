import streamlit as st
import os
from dotenv import load_dotenv
import agent

load_dotenv()

st.set_page_config(
    page_title="BYS Setting Agent — Revenew",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    /* Global */
    .stApp { background-color: #0f1117; }

    /* Message box */
    .msg-box {
        background: #1e2130;
        border-left: 4px solid #3b82f6;
        padding: 1rem 1.2rem;
        border-radius: 0 10px 10px 0;
        font-size: 1rem;
        line-height: 1.7;
        color: #e2e8f0;
        white-space: pre-wrap;
        margin: 0.5rem 0;
    }
    .coaching-box {
        background: #1a2535;
        border: 1px solid #2563eb33;
        border-radius: 8px;
        padding: 0.8rem 1rem;
        font-size: 0.88rem;
        color: #94a3b8;
        margin-top: 0.5rem;
    }
    .rule-pill {
        display: inline-block;
        background: #7f1d1d22;
        border: 1px solid #ef444444;
        color: #fca5a5;
        border-radius: 20px;
        padding: 2px 10px;
        font-size: 0.78rem;
        margin: 2px;
    }
    .ok-pill {
        display: inline-block;
        background: #14532d22;
        border: 1px solid #22c55e44;
        color: #86efac;
        border-radius: 20px;
        padding: 2px 10px;
        font-size: 0.78rem;
        margin: 2px;
    }
    .word-badge {
        font-size: 0.8rem;
        font-weight: 600;
        padding: 3px 10px;
        border-radius: 20px;
    }
    .word-ok { background: #14532d; color: #86efac; }
    .word-warn { background: #713f12; color: #fde68a; }
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background: #1e2130;
        border-radius: 8px;
        color: #94a3b8;
        padding: 6px 16px;
    }
    .stTabs [aria-selected="true"] {
        background: #1d4ed8 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🎯 BYS Setting Agent")
    st.markdown("**Campagne active :** Revenew 🚀")
    st.markdown("---")

    st.markdown("### 🔗 Liens essentiels")
    st.markdown("📅 [Agenda Mathéo](https://cal.com/matheo.bonnet/consultative-meeting)")
    st.markdown("📋 [Questionnaire Tally](https://tally.so/r/44EbKk)")
    st.markdown("🌐 [Revenew](https://revenew.tech/)")
    st.markdown("🏢 [BYS](https://buildyoursales.tech/en)")
    st.markdown("---")

    st.markdown("### ⚡ Règle absolue")
    st.markdown("""
    <div style="background:#1e2130;border-left:3px solid #ef4444;padding:10px 12px;border-radius:0 8px 8px 0;font-size:0.85rem;color:#e2e8f0;">
    ❌ <b>JAMAIS pitcher</b><br><br>
    ✅ Parler de <b>LEURS enjeux</b><br>
    ✅ Revenew = "on construit quelque chose, votre retour compte"<br>
    ✅ Objectif : <b>RDV 20 min</b> ou <b>questionnaire</b>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 🎯 ICP Revenew")
    for persona in ["Sales Ops / Revenue Ops", "Directeurs & managers SDR",
                     "Agences marketing outbound", "Fractional Head of Sales",
                     "Head of Growth / Growth Ops", "Consultants GTM B2B"]:
        st.markdown(f"• {persona}")
    st.markdown("---")

    st.markdown("### 📊 KPIs cibles")
    st.markdown("• Taux réponse 1er msg : **30-50%**")
    st.markdown("• Conversion réponse → RDV : **20-30%**")
    st.markdown("• No-show : **< 20%**")
    st.markdown("---")

    api_key_input = st.text_input(
        "🔑 Clé API Anthropic",
        type="password",
        value=os.getenv("ANTHROPIC_API_KEY", ""),
        help="Votre clé API Anthropic (commence par sk-ant-)",
    )
    if api_key_input:
        os.environ["ANTHROPIC_API_KEY"] = api_key_input

# ─── HEADER ─────────────────────────────────────────────────────────────────

st.markdown("# 🎯 Agent Setting LinkedIn — Revenew")
st.markdown("*Assistant IA pour les setters BYS | Représente Mathéo Bonnet sur LinkedIn*")
st.markdown("---")

# ─── TABS ────────────────────────────────────────────────────────────────────

tab1, tab2, tab3, tab4 = st.tabs([
    "✉️  Icebreaker",
    "💬  Conversation",
    "🔄  Relance",
    "❓  Coach",
])


def check_api_key() -> bool:
    if not os.getenv("ANTHROPIC_API_KEY"):
        st.error("⚠️ Clé API manquante — entrez-la dans la barre latérale à gauche.")
        return False
    return True


def render_message(text: str, limit: int | None = None):
    """Render generated message with word count badge."""
    st.markdown(f'<div class="msg-box">{text}</div>', unsafe_allow_html=True)
    if limit:
        words = len(text.split())
        badge_class = "word-ok" if words <= limit else "word-warn"
        icon = "✅" if words <= limit else "⚠️"
        st.markdown(
            f'<span class="word-badge {badge_class}">{icon} {words} mots (max {limit})</span>',
            unsafe_allow_html=True,
        )
    st.text_area("📋 Copier :", value=text, height=80, key=f"copy_{hash(text)}")


# ─── TAB 1 : ICEBREAKER ──────────────────────────────────────────────────────

with tab1:
    st.subheader("Générer un icebreaker LinkedIn")
    st.caption("Premier message — déclencher une réponse, rien d'autre. Max 50 mots, jamais pitcher.")

    col1, col2 = st.columns(2)
    with col1:
        ib_name = st.text_input("Prénom + Nom *", placeholder="ex : Sophie Martin")
        ib_headline = st.text_input(
            "Titre LinkedIn *",
            placeholder="ex : Head of Sales Ops @ Contentsquare",
        )
        ib_industry = st.text_input(
            "Secteur *", placeholder="ex : SaaS B2B / Scale-up tech"
        )
        ib_source = st.selectbox(
            "Source du contact",
            [
                "⭐⭐⭐⭐⭐ Nouvelle connexion reçue (intent fort)",
                "⭐⭐⭐⭐⭐ Visite de profil reçue",
                "⭐⭐⭐⭐⭐ Réaction à un post BYS/Mathéo",
                "⭐⭐⭐ Réseau 1er degré non contacté",
                "⭐⭐ Connexion froide acceptée",
            ],
        )

    with col2:
        ib_posts = st.text_area(
            "Posts récents (résumés)",
            placeholder="ex: A posté sur la structuration des équipes SDR...\nA commenté sur les outils RevOps...",
            height=110,
        )
        ib_experiences = st.text_area(
            "Expériences clés",
            placeholder="ex: 3 ans Head of Sales @ Qonto, avant SDR Manager @ Aircall",
            height=80,
        )

    if st.button("🚀 Générer l'icebreaker", type="primary", use_container_width=True):
        if not all([ib_name, ib_headline, ib_industry]):
            st.error("Remplissez au moins le nom, le titre et le secteur.")
        elif check_api_key():
            prompt = f"""Génère un icebreaker LinkedIn pour ce prospect. Retourne UNIQUEMENT le message.

Données prospect :
- Nom : {ib_name}
- Titre : {ib_headline}
- Posts récents : {ib_posts or "Non renseigné"}
- Expériences : {ib_experiences or "Non renseigné"}
- Secteur : {ib_industry}
- Source : {ib_source}

Règles : 50 mots max, jamais pitcher, jamais parler de Revenew ou BYS, question ouverte à la fin, ton oral pair à pair, vouvoiement."""

            with st.spinner("Génération en cours..."):
                placeholder = st.empty()
                full = ""
                for chunk in agent.stream_message(prompt):
                    full += chunk
                    placeholder.markdown(
                        f'<div class="msg-box">{full}▌</div>', unsafe_allow_html=True
                    )
                placeholder.empty()
                render_message(full, limit=50)

    st.markdown("---")
    st.markdown("**Bons exemples d'icebreakers :**")
    examples = [
        "\"Votre post sur les 3 erreurs d'acquisition en agence m'a interpellé — vous touchez quelque chose que peu de gens formulent clairement. Vous avez trouvé une approche pour régler ça ?\"",
        "\"Votre transition de Qonto vers la consultance, c'est un choix que j'entends de plus en plus chez les profils sales ops. C'est quoi qui vous a décidé ?\"",
        "\"Vous menez une équipe SDR chez une scale-up en même temps que vous gérez le stack outbound — ça ressemble à quoi en pratique ?\"",
    ]
    for ex in examples:
        st.markdown(f'<div class="coaching-box">{ex}</div>', unsafe_allow_html=True)


# ─── TAB 2 : CONVERSATION ────────────────────────────────────────────────────

with tab2:
    st.subheader("Répondre dans une conversation en cours")
    st.caption(
        "Colle la conversation LinkedIn — l'agent analyse et te dit quoi envoyer."
    )

    conv_text = st.text_area(
        "Conversation LinkedIn (colle l'intégralité) *",
        placeholder="""Exemple :
MOI : Votre post sur la structuration SDR m'a interpellé. C'est quelque chose qui s'est accéléré dans votre secteur récemment ?
PROSPECT : Oui carrément, on essaie justement de mieux structurer ça. Vous êtes dans quel domaine ?
MOI : ...""",
        height=220,
    )

    col1, col2 = st.columns([3, 1])
    with col1:
        conv_context = st.text_input(
            "Contexte additionnel (optionnel)",
            placeholder="ex: Semble intéressé, mentionne un problème de data, 50 personnes dans l'équipe",
        )
    with col2:
        conv_stage = st.selectbox(
            "Étape",
            ["Qualification", "Apport de valeur", "Proposition de RDV", "Objection"],
        )

    if st.button("💬 Générer la réponse", type="primary", use_container_width=True):
        if not conv_text.strip():
            st.error("Colle la conversation avant de générer.")
        elif check_api_key():
            prompt = f"""Voici une conversation LinkedIn en cours. Génère la prochaine réponse optimale.

Conversation :
{conv_text}

Étape actuelle : {conv_stage}
{f"Contexte : {conv_context}" if conv_context else ""}

Format de sortie OBLIGATOIRE :
[Le message à envoyer]
---
[2-3 lignes de coaching sur pourquoi cette approche]

Règles pour le message :
- Qualification = max 30 mots, question ouverte sur leurs enjeux outbound/data
- Valeur = insight lié à Revenew/outbound sans pitcher les features, max 40 mots
- RDV = lier leur problème identifié à ce qu'on construit, proposer 20 min ou questionnaire Tally
- Jamais commencer par un verbe
- Jamais "notre solution/offre/agence"
- Ton oral"""

            with st.spinner("Analyse de la conversation..."):
                placeholder = st.empty()
                full = ""
                for chunk in agent.stream_message(prompt):
                    full += chunk
                    placeholder.markdown(full + "▌")
                placeholder.empty()

            parts = full.split("---", 1)
            message_part = parts[0].strip()
            coaching_part = parts[1].strip() if len(parts) > 1 else ""

            st.markdown("**Message à envoyer :**")
            render_message(message_part, limit=40)

            if coaching_part:
                st.markdown("**Coaching :**")
                st.markdown(
                    f'<div class="coaching-box">💡 {coaching_part}</div>',
                    unsafe_allow_html=True,
                )


# ─── TAB 3 : RELANCE ─────────────────────────────────────────────────────────

with tab3:
    st.subheader("Générer une relance")
    st.markdown(
        '<span class="rule-pill">❌ JAMAIS mentionner le silence</span>'
        '<span class="rule-pill">❌ JAMAIS "je relance"</span>'
        '<span class="ok-pill">✅ Angle totalement différent</span>'
        '<span class="ok-pill">✅ 25 mots max</span>',
        unsafe_allow_html=True,
    )
    st.markdown("")

    col1, col2 = st.columns([2, 1])
    with col1:
        rel_first_msg = st.text_area(
            "Premier message envoyé *",
            placeholder="Colle ici le message initial que tu as envoyé...",
            height=110,
        )
        rel_profile = st.text_input(
            "Infos prospect *",
            placeholder="ex: Head of Sales Ops, SaaS B2B, a posté sur RevOps récemment, 80 personnes",
        )
    with col2:
        rel_days = st.number_input(
            "Jours sans réponse", min_value=1, max_value=30, value=5
        )
        rel_number = st.radio(
            "Numéro de relance",
            ["Relance 1 (sur 2 max)", "Relance 2 — DERNIÈRE"],
        )
        if "DERNIÈRE" in rel_number:
            st.warning("⚠️ Après cette relance : on classe et on passe. Ne pas insister.")

    if st.button("🔄 Générer la relance", type="primary", use_container_width=True):
        if not rel_first_msg.strip() or not rel_profile.strip():
            st.error("Premier message et infos prospect requis.")
        elif check_api_key():
            prompt = f"""Génère une relance LinkedIn. Retourne UNIQUEMENT le message.

Premier message envoyé : {rel_first_msg}
Profil prospect : {rel_profile}
Jours sans réponse : {rel_days}
Numéro de relance : {rel_number}

RÈGLES ABSOLUES :
- JAMAIS mentionner qu'il n'a pas répondu
- JAMAIS "je relance", "tu n'as pas vu", "petit follow-up", "je reviens vers toi"
- Angle TOTALEMENT différent du premier message
- 25 mots maximum
- Ton oral, vouvoiement
- Ouvrir sur quelque chose de nouveau (actualité du secteur, post récent, observation)"""

            with st.spinner("Génération de la relance..."):
                placeholder = st.empty()
                full = ""
                for chunk in agent.stream_message(prompt):
                    full += chunk
                    placeholder.markdown(
                        f'<div class="msg-box">{full}▌</div>', unsafe_allow_html=True
                    )
                placeholder.empty()
                render_message(full, limit=25)


# ─── TAB 4 : COACH Q&A ───────────────────────────────────────────────────────

with tab4:
    st.subheader("Coach — Pose ta question")
    st.caption(
        "Demande conseil sur n'importe quelle situation de setting, l'angle Revenew, ou la méthodologie BYS."
    )

    st.markdown("**Questions fréquentes :**")
    faq = [
        "Le prospect demande le prix — je réponds quoi ?",
        "Il dit 'pas intéressé' — comment sortir proprement ?",
        "Comment introduire Revenew sans que ça sonne comme un pitch ?",
        "Il demande 'vous faites quoi exactement ?' — que dire ?",
        "Quand proposer le questionnaire Tally plutôt qu'un RDV ?",
        "Il travaille déjà avec un concurrent — comment répondre ?",
        "Comment savoir si un prospect est bien dans l'ICP Revenew ?",
        "Il dit 'envoyez-moi plus d'infos' — je fais quoi ?",
    ]

    cols = st.columns(2)
    clicked_faq = None
    for i, q in enumerate(faq):
        with cols[i % 2]:
            if st.button(q, key=f"faq_{i}", use_container_width=True):
                clicked_faq = q

    st.markdown("")
    coach_q = st.text_area(
        "Ou pose ta propre question :",
        value=clicked_faq or st.session_state.get("coach_q_prefill", ""),
        placeholder="ex: Le prospect semble intéressé mais hésite à bloquer un créneau — que faire ?",
        height=100,
        key="coach_input",
    )

    if clicked_faq:
        st.session_state["coach_q_prefill"] = clicked_faq

    if st.button("🤔 Obtenir un conseil", type="primary", use_container_width=True):
        question = coach_q.strip()
        if not question:
            st.error("Pose ta question d'abord.")
        elif check_api_key():
            with st.spinner("Réflexion en cours..."):
                placeholder = st.empty()
                full = ""
                for chunk in agent.stream_message(question):
                    full += chunk
                    placeholder.markdown(full + "▌")
                placeholder.markdown(full)

    st.markdown("---")
    st.markdown("### 📖 Mémo rapide — Situations spéciales")

    situations = {
        "❓ 'Vous faites quoi ?'": "Répondre simplement sur Revenew (on construit une plateforme outbound, on cherche des retours terrain) puis relancer sur leur situation : \"C'est quoi votre stack outbound en ce moment ?\"",
        "💰 'Combien ça coûte ?'": "\"Ça dépend du contexte, on en parle sur le call de 20 min.\" — Jamais donner un prix en DM.",
        "🚫 'Pas intéressé'": "\"Pas de souci. Si ça évolue, je suis là.\" — Sortie propre, pas de contre-argumentaire.",
        "📄 'Envoyez plus d'infos'": "\"Je préfère vous montrer directement — 20 min cette semaine ?\" ou envoyer le lien questionnaire Tally.",
        "🤝 'Je travaille déjà avec quelqu'un'": "\"Ça se passe bien ? Je demande parce qu'on travaille souvent en complément.\"",
    }

    for title, content in situations.items():
        with st.expander(title):
            st.markdown(f'<div class="coaching-box">{content}</div>', unsafe_allow_html=True)
