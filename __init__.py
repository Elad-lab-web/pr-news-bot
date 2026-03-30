"""
clients/config.py
הגדרת כל לקוחות משרד יחסי הציבור.
כדי להוסיף לקוח — העתק בלוק קיים ומלא את הפרטים.
REPLACE_XXX = החלף במספר ה-chat_id של הלקוח בטלגרם.
"""

CLIENTS = [
    {
        "id": "bit",
        "name": "Bit",
        "telegram_chat_id": "REPLACE_BIT",
        "company_names": ["Bit", "ביט", "אפליקציית ביט"],
        "keywords": [
            "אפליקציות תשלומים", "תשלומים דיגיטליים", "העברת כסף",
            "ארנקים דיגיטליים", "P2P payments", "פייבוקס", "Apple Pay",
            "Google Pay", "ארנקים סלולריים", "סליקה", "פינטק צרכני",
            "תשלומים ללא מזומן", "QR payments",
        ],
        "industries": ["finance", "tech"],
        "competitors": ["PayBox", "Apple Pay", "Google Pay", "PayPal"],
        "active": True,
    },
    {
        "id": "poalim_tech",
        "name": "Poalim Tech",
        "telegram_chat_id": "REPLACE_POALIM",
        "company_names": ["Poalim Tech", "פועלים טק", "בנק הפועלים"],
        "keywords": [
            "סטארטאפים", "גיוסי כספים", "Seed", "Series A", "Series B",
            "Venture Capital", "רשות החדשנות", "השקעות", "קרנות הון סיכון",
            "CFO", "SaaS", "יזמות", "אקזיטים", "הייטק ישראלי", "משבר הייטק",
        ],
        "industries": ["tech", "finance"],
        "competitors": ["לאומיטק", "דיסקונט הייטק", "Silicon Valley Bank"],
        "active": True,
    },
    {
        "id": "gett",
        "name": "Gett",
        "telegram_chat_id": "REPLACE_GETT",
        "company_names": ["Gett", "גט"],
        "keywords": [
            "מוניות", "תחבורה שיתופית", "mobility", "ride hailing",
            "תחבורה עירונית", "אפליקציות תחבורה", "נסיעות עסקיות",
            "נהגי מונית", "משרד התחבורה", "איגוד נהגי המוניות",
        ],
        "industries": ["tech"],
        "competitors": ["Uber", "Bolt", "Yango", "Lyft"],
        "active": True,
    },
    {
        "id": "adidas",
        "name": "adidas ישראל",
        "telegram_chat_id": "REPLACE_ADIDAS",
        "company_names": ["adidas", "אדידס"],
        "keywords": [
            "ספורט", "אופנה", "סניקרס", "שיתופי פעולה", "קיימות באופנה",
            "קמפיין אופנה", "מותגים בינלאומיים", "חנות אופנה חדשה",
            "השקות באופנה", "אלקטרה צריכה", "ביגוד כדורגל", "ביגוד כדורסל",
        ],
        "industries": [],
        "competitors": ["Nike", "Puma", "Under Armour", "MGS"],
        "active": True,
    },
    {
        "id": "leket",
        "name": "לקט ישראל",
        "telegram_chat_id": "REPLACE_LEKET",
        "company_names": ["לקט ישראל", "Leket Israel"],
        "keywords": [
            "ביטחון תזונתי", "תרומות מזון", "עוני", "קיימות",
            "בזבוז מזון", "חקלאות", "הצלת מזון", "תרומה",
        ],
        "industries": ["food"],
        "competitors": ["פתחון לב", "לתת"],
        "active": True,
    },
    {
        "id": "tmir",
        "name": "תאגיד המחזור תמיר",
        "telegram_chat_id": "REPLACE_TMIR",
        "company_names": ["תמיר", "TMIR", "תאגיד המחזור תמיר"],
        "keywords": [
            "מחזור", "פסולת", "איכות סביבה", "קיימות",
            "חוק הפיקדון", "אריזות", "פלסטיק",
        ],
        "industries": [],
        "competitors": ["המשרד להגנת הסביבה", "חברות מחזור פרטיות"],
        "active": True,
    },
    {
        "id": "angel",
        "name": "מאפיית אנג'ל",
        "telegram_chat_id": "REPLACE_ANGEL",
        "company_names": ["אנג'ל", "Angel Bakeries", "מאפיית אנג'ל", "ירון אנג'ל", "משפחת אנג'ל"],
        "keywords": [
            "מזון", "לחם", "קמעונאות מזון", "יוקר המחיה",
            "חומרי גלם", "שרשרת אספקה", "לחם פרו", "לחם חלבון",
            "שוק הלחם", "חמץ", "מאפייה", "קונדיטוריה",
        ],
        "industries": ["food"],
        "competitors": ["אגמי", "ברמן", "דוידוביץ'"],
        "active": True,
    },
    {
        "id": "milt",
        "name": "ד\"ר ערן מילט",
        "telegram_chat_id": "REPLACE_MILT",
        "company_names": ["ד\"ר ערן מילט", "Dr. Eran Milt", "מילט"],
        "keywords": [
            "כירורגיה פלסטית", "טיפולים אסתטיים", "האיגוד הישראלי לכירורגיה פלסטית",
            "חדשנות רפואית", "ניתוחים לעיצוב הגוף", "מתיחת בטן",
            "הזרקת שומן עצמי", "ניתוחי חזה", "ניתוחי פנים וצוואר", "תיירות מרפא",
        ],
        "industries": ["health"],
        "competitors": ["דב קליין", "רוני מוסקונה", "איל וינקלר", "אסותא", "הרצליה מדיקל"],
        "active": True,
    },
    {
        "id": "apollo",
        "name": "Apollo Power",
        "telegram_chat_id": "REPLACE_APOLLO",
        "company_names": ["Apollo Power", "אפולו פאוור"],
        "keywords": [
            "אנרגיה סולארית", "קלינטק", "קיימות", "אנרגיה ירוקה",
            "חדשנות", "פאנלים סולאריים",
        ],
        "industries": ["tech"],
        "competitors": ["SolarEdge", "Enlight", "דוראל"],
        "active": True,
    },
    {
        "id": "technion_alumni",
        "name": "ארגון בוגרי הטכניון",
        "telegram_chat_id": "REPLACE_TECHNION",
        "company_names": ["ארגון בוגרי הטכניון", "Technion Alumni", "טכניון"],
        "keywords": [
            "בוגרים", "הייטק", "חדשנות", "קהילה מקצועית",
            "אקדמיה", "יזמות", "טכנולוגיה", "טכניון", "בינה מלאכותית",
        ],
        "industries": ["tech"],
        "competitors": [],
        "active": True,
    },
    {
        "id": "zooz",
        "name": "ZOOZ Strategy",
        "telegram_chat_id": "REPLACE_ZOOZ",
        "company_names": ["ZOOZ Strategy", "זוז סטרטג'י", "ג'ורדן פריד"],
        "keywords": [
            "ביטקוין", "אוצר ביטקוין", "בורסה", "נאסד\"ק",
            "קריפטו", "מטבעות דיגיטליים", "אנרגיה",
        ],
        "industries": ["finance", "tech"],
        "competitors": ["MicroStrategy", "Marathon Digital", "Riot Platforms"],
        "active": True,
    },
    {
        "id": "grow",
        "name": "Grow",
        "telegram_chat_id": "REPLACE_GROW",
        "company_names": ["Grow", "גרו"],
        "keywords": [
            "סליקות", "רפורמה בנקאית", "רפורמה שוק ההון", "פינטק",
        ],
        "industries": ["finance", "tech"],
        "competitors": [],
        "active": True,
    },
    {
        "id": "hapoel_jerusalem",
        "name": "הפועל ירושלים",
        "telegram_chat_id": "REPLACE_HAPOEL",
        "company_names": ["הפועל ירושלים", "Hapoel Jerusalem"],
        "keywords": [
            "ספורט", "ליגה", "אוהדים", "משחקים", "חסויות",
            "שידורים", "כדורסל", "כדורגל",
        ],
        "industries": [],
        "competitors": ["מכבי תל אביב"],
        "active": True,
    },
    {
        "id": "bluestone",
        "name": "Bluestone Live Nation",
        "telegram_chat_id": "REPLACE_BLUESTONE",
        "company_names": ["Bluestone", "בלוסטון", "Live Nation ישראל", "גיי בסר", "שי מור יוסף"],
        "keywords": [
            "הופעות", "מוזיקה", "אמנים", "כרטיסים", "אירועים",
            "פסטיבלים", "תרבות", "מופעים", "אנטרטיינמנט",
            "פארק הירקון", "קו רקיע",
        ],
        "industries": [],
        "competitors": ["זאפה", "שוקי וייס", "Live Nation"],
        "active": True,
    },
    {
        "id": "cbc",
        "name": "CBC Group",
        "telegram_chat_id": "REPLACE_CBC",
        "company_names": ["CBC", "החברה המרכזית למשקאות קלים", "קוקה קולה ישראל", "טרה", "דודי ורטהיים", "משפחת ורטהיים"],
        "keywords": [
            "משקאות קלים", "בירה", "חלב", "מותגים", "קמעונאות",
            "שוק המזון", "בריאות", "משקאות חלבון", "ללא לקטוז",
            "משקאות ממותקים", "מים", "מיצים", "יין", "יקב",
            "וודקה", "ויסקי", "ספירטים", "בירה ישראלית", "בירת קראפט",
            "תחליפי חלב", "יוגורט", "רשות התחרות", "משקאות אנרגיה",
        ],
        "industries": ["food"],
        "competitors": ["טמפו", "יפאורה תבורי", "שטראוס", "מחלבות גד", "יטבתה", "מי עדן", "יקב ברקן"],
        "active": True,
    },
    {
        "id": "biolight",
        "name": "BioLight",
        "telegram_chat_id": "REPLACE_BIOLIGHT",
        "company_names": ["BioLight", "ביולייט"],
        "keywords": [
            "ביוטכנולוגיה", "מכשור רפואי", "סטארטאפים רפואיים",
            "השקעות", "ניסויים קליניים", "מחקר", "עיניים", "דיאגנוסטיקה",
        ],
        "industries": ["health", "tech"],
        "competitors": ["קרנות ביומד", "חברות השקעה במדעי החיים"],
        "active": True,
    },
    {
        "id": "nfx",
        "name": "NFX",
        "telegram_chat_id": "REPLACE_NFX",
        "company_names": ["NFX", "אנפקס", "גיגי לוי וייס", "שרי ברונפלד"],
        "keywords": [
            "קרן הון סיכון", "סיד", "השקעות", "הייטק", "יזמות",
            "גיימינג", "לונג'ביטי", "חדשנות", "סטרטאפ",
            "רשות החדשנות", "סיליקון ואלי", "משקיעים", "גיוס", "אקוסיסטם",
        ],
        "industries": ["tech", "finance"],
        "competitors": ["Aleph", "TLV Partners", "Vertex Ventures", "Grove Ventures", "Sequoia Capital", "a16z"],
        "active": True,
    },
]


def get_active_clients():
    return [c for c in CLIENTS if c.get("active", True)]


def get_all_industries():
    industries = set()
    for client in get_active_clients():
        industries.update(client.get("industries", []))
    return list(industries)
