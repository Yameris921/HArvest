# HArvest

> 🇫🇷 Français | 🇬🇧 [English](#english)

---

## 🇫🇷 Français

Panneau Home Assistant pour visualiser et exporter toutes vos entités vers **Excel, CSV ou JSON** — directement depuis la barre latérale.

### Fonctionnalités

- **Langue automatique** : détecte la langue de HA ou du navigateur (FR / EN), avec bascule manuelle
- Connexion automatique (token HA lu depuis le navigateur)
- Filtres : domaine, état, recherche texte libre
- Tri sur toutes les colonnes
- Colonnes activables/désactivables
- Export Excel `.xlsx` : onglet global + un onglet par domaine + onglet résumé
- Export CSV (séparateur adapté à la langue : `;` en FR, `,` en EN)
- Export JSON (données brutes)

### Installation via HACS

1. HACS → **Intégrations** → ⋮ → *Dépôts personnalisés*
2. Ajouter l'URL du dépôt, catégorie **Integration**
3. Installer **HArvest**
4. Ajouter dans `configuration.yaml` :
   ```yaml
   harvest:
   ```
5. Redémarrer Home Assistant
6. Le panneau **HArvest** (icône 🌱) apparaît dans la barre latérale

### Installation manuelle

1. Copier `custom_components/harvest/` dans `<config>/custom_components/`
2. Ajouter `harvest:` dans `configuration.yaml`
3. Redémarrer Home Assistant

---

## 🇬🇧 English <a name="english"></a>

Home Assistant panel to visualise and export all your entities to **Excel, CSV or JSON** — directly from the sidebar.

### Features

- **Automatic language** : detects HA or browser language (FR / EN), with manual toggle
- Auto-login (reads HA token from the browser)
- Filters: domain, state, full-text search
- Sortable columns
- Show/hide columns individually
- Excel `.xlsx` export: global sheet + one sheet per domain + summary sheet
- CSV export (separator adapts to language: `;` for FR, `,` for EN)
- JSON export (raw data)

### Installation via HACS

1. HACS → **Integrations** → ⋮ → *Custom repositories*
2. Add the repository URL, category **Integration**
3. Install **HArvest**
4. Add to `configuration.yaml`:
   ```yaml
   harvest:
   ```
5. Restart Home Assistant
6. The **HArvest** panel (🌱 icon) appears in the sidebar

### Manual installation

1. Copy `custom_components/harvest/` to `<config>/custom_components/`
2. Add `harvest:` to `configuration.yaml`
3. Restart Home Assistant
