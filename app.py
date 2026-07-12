from flask import Flask, request

app = Flask(__name__)
users = {}

PRODUCTS = [
             ("Face Facts Vitamin C Serum", "Face Facts", "Brightening serum for dull skin.", "سيروم يساعد على إشراق البشرة الباهتة.", "Apply a few drops daily.", "توضع بضع قطرات يومياً.", "/static/products/1.jpg"),
    ("Face Facts Hyaluronic Acid Serum", "Face Facts", "Hydrating serum for soft skin.", "سيروم ترطيب يساعد على نعومة البشرة.", "Apply to clean skin before moisturizer.", "يوضع على بشرة نظيفة قبل المرطب.", "/static/products/2.jfif"),
    ("Face Facts Niacinamide Serum", "Face Facts", "Helps reduce shine and improve skin texture.", "يساعد على تقليل اللمعان وتحسين ملمس البشرة.", "Apply once daily.", "يوضع مرة يومياً.", "/static/products/3.png"),
    ("Face Facts Retinol Serum", "Face Facts", "Night serum for smoother looking skin.", "سيروم ليلي يساعد البشرة أن تبدو أنعم.", "Use at night and apply sunscreen in the morning.", "يستخدم ليلاً مع وضع واقي شمس صباحاً.", "/static/products/4.png"),
    ("Face Facts Vitamin C Cleanser", "Face Facts", "Gentle cleanser for brighter skin.", "غسول لطيف لبشرة أكثر إشراقاً.", "Use with water then rinse.", "يستخدم مع الماء ثم يغسل.", "/static/products/5.png"),
    ("Face Facts Hydrating Cleanser", "Face Facts", "Cleanses skin without dryness.", "ينظف البشرة دون أن يسبب جفافاً.", "Use morning and night.", "يستخدم صباحاً ومساءً.", "/static/products/6.png"),
("Face Facts Vitamin C Face Mask", "Face Facts", "Refreshing mask for glow.", "ماسك منعش لإشراق البشرة.", "Apply on clean face then wash.", "يوضع على وجه نظيف ثم يغسل.", "/static/products/7.png"),

("Face Facts Aloe Vera Gel", "Face Facts", "Soothing gel for skin comfort.", "جل مهدئ يمنح راحة للبشرة.", "Apply to irritated or dry areas.", "يوضع على المناطق الجافة أو المتهيجة.", "/static/products/8.png"),

("Face Facts Micellar Water", "Face Facts", "Removes makeup and impurities.", "يزيل المكياج والشوائب.", "Use with cotton pad.", "يستخدم بقطنة.", "/static/products/9.png"),

("Face Facts Clay Mask", "Face Facts", "Purifying mask for oily skin.", "ماسك منقٍ للبشرة الدهنية.", "Apply, leave to dry, then rinse.", "يوضع حتى يجف ثم يغسل.", "/static/products/10.png"),

("Face Facts Collagen Serum", "Face Facts", "Helps skin look smoother and fresher.", "يساعد البشرة أن تبدو أنعم وأكثر نضارة.", "Apply daily before cream.", "يوضع يومياً قبل الكريم.", "/static/products/11.png"),

("Face Facts Tea Tree Serum", "Face Facts", "Care for blemish-prone skin.", "عناية للبشرة المعرضة للحبوب.", "Apply a small amount on clean skin.", "توضع كمية قليلة على بشرة نظيفة.", "/static/products/12.png"),

("Face Facts Brightening Toner", "Face Facts", "Helps refresh and tone skin.", "يساعد على إنعاش وتوازن البشرة.", "Use after cleansing.", "يستخدم بعد الغسول.", "/static/products/13.png"),

("Face Facts Hydrating Toner", "Face Facts", "Hydrating toner for daily use.", "تونر مرطب للاستخدام اليومي.", "Apply with cotton pad.", "يوضع بقطنة.", "/static/products/14.png"),

("Face Facts Eye Gel", "Face Facts", "Cooling care for tired eyes.", "عناية مبردة لمنطقة العين.", "Apply gently around eyes.", "يوضع بلطف حول العينين.", "/static/products/15.png"),

("Face Facts Day Cream", "Face Facts", "Daily cream for soft skin.", "كريم يومي لبشرة ناعمة.", "Apply every morning.", "يوضع كل صباح.", "/static/products/16.png"),

("Face Facts Night Cream", "Face Facts", "Night care for skin comfort.", "عناية ليلية لراحة البشرة.", "Apply before sleep.", "يوضع قبل النوم.", "/static/products/17.png"),

("Face Facts SPF Moisturizer", "Face Facts", "Daily moisturizer with sun protection.", "مرطب يومي مع حماية من الشمس.", "Apply before sun exposure.", "يوضع قبل التعرض للشمس.", "/static/products/18.png"),

("Face Facts Cleansing Balm", "Face Facts", "Melts makeup and cleans skin.", "يزيل المكياج وينظف البشرة.", "Massage on dry skin then rinse.", "يدلك على بشرة جافة ثم يغسل.", "/static/products/19.png"),

("Face Facts Pore Strips", "Face Facts", "Helps remove impurities from nose area.", "يساعد على إزالة الشوائب من منطقة الأنف.", "Apply on wet nose then remove.", "يوضع على الأنف المبلل ثم يزال.", "/static/products/20.png"),

("Face Facts Sheet Mask", "Face Facts", "Hydrating sheet mask.", "ماسك ورقي مرطب.", "Apply for 10-15 minutes.", "يوضع لمدة 10-15 دقيقة.", "/static/products/21.png"),

("Face Facts Under Eye Patches", "Face Facts", "Helps refresh under eye area.", "يساعد على إنعاش منطقة تحت العين.", "Place under eyes for minutes.", "يوضع تحت العين لعدة دقائق.", "/static/products/22.png"),

("Face Facts Lip Balm", "Face Facts", "Moisturizes dry lips.", "يرطب الشفاه الجافة.", "Apply whenever needed.", "يوضع عند الحاجة.", "/static/products/23.png"),

("Face Facts Hand Cream", "Face Facts", "Softens dry hands.", "ينعم اليدين الجافتين.", "Apply to hands daily.", "يوضع على اليدين يومياً.", "/static/products/24.png"),

("Face Facts Body Lotion", "Face Facts", "Moisturizes body skin.", "يرطب بشرة الجسم.", "Apply after shower.", "يوضع بعد الاستحمام.", "/static/products/25.png"),

("Face Facts Foot Cream", "Face Facts", "Care for dry feet.", "عناية للقدمين الجافتين.", "Apply to feet daily.", "يوضع على القدمين يومياً.", "/static/products/26.png"),

("Face Facts Makeup Remover Wipes", "Face Facts", "Removes makeup quickly.", "يزيل المكياج بسرعة.", "Use one wipe on face.", "تستخدم منديل واحد للوجه.", "/static/products/27.png"),

("Face Facts Cleansing Foam", "Face Facts", "Foam cleanser for daily use.", "غسول رغوي للاستخدام اليومي.", "Massage then rinse.", "يدلك ثم يغسل.", "/static/products/28.png"),

("Face Facts Glow Drops", "Face Facts", "Gives skin a glowing look.", "يعطي البشرة مظهراً مشرقاً.", "Apply a few drops before cream.", "توضع بضع قطرات قبل الكريم.", "/static/products/29.png"),

("CeraVe Foaming Facial Cleanser", "CeraVe", "Foaming cleanser for normal to oily skin.", "غسول رغوي للبشرة العادية إلى الدهنية.", "Use morning and evening with water.", "يستخدم صباحاً ومساءً مع الماء.", "/static/products/30.png"),

("CeraVe Hydrating Cleanser", "CeraVe", "Hydrating cleanser for normal to dry skin.", "غسول مرطب للبشرة العادية إلى الجافة.", "Massage gently then rinse.", "يدلك بلطف ثم يغسل.", "/static/products/31.png"),

("CeraVe SA Smoothing Cleanser", "CeraVe", "Salicylic acid cleanser for rough skin.", "غسول بحمض الساليسيليك للبشرة الخشنة.", "Use once or twice daily.", "يستخدم مرة أو مرتين يومياً.", "/static/products/32.png"),

("CeraVe Moisturizing Cream", "CeraVe", "Rich moisturizer for face and body.", "كريم مرطب للوجه والجسم.", "Apply whenever needed.", "يوضع عند الحاجة.", "/static/products/33.png"),

("CeraVe Daily Moisturizing Lotion", "CeraVe", "Lightweight daily moisturizer.", "لوشن مرطب خفيف للاستخدام اليومي.", "Apply to clean skin.", "يوضع على بشرة نظيفة.", "/static/products/34.png"),

("CeraVe Facial Moisturizing Lotion AM SPF30", "CeraVe", "Morning moisturizer with SPF 30.", "مرطب صباحي مع واقي شمس SPF30.", "Apply every morning.", "يوضع كل صباح.", "/static/products/35.png"),

("CeraVe Facial Moisturizing Lotion PM", "CeraVe", "Night moisturizer with ceramides.", "مرطب ليلي غني بالسيراميدات.", "Apply before bedtime.", "يوضع قبل النوم.", "/static/products/36.png"),
("CeraVe Eye Repair Cream", "CeraVe", "Helps reduce puffiness around eyes.", "يساعد على تقليل الانتفاخ حول العين.", "Apply gently around eyes.", "يوضع بلطف حول العينين.", "/static/products/37.png"),

("CeraVe Healing Ointment", "CeraVe", "Protective ointment for dry skin.", "مرهم واقٍ للبشرة الجافة.", "Apply to dry areas.", "يوضع على المناطق الجافة.", "/static/products/38.png"),

("CeraVe Hydrating Hyaluronic Acid Serum", "CeraVe", "Hydrating serum with hyaluronic acid.", "سيروم مرطب بحمض الهيالورونيك.", "Apply before moisturizer.", "يوضع قبل المرطب.", "/static/products/39.png"),

("CeraVe Acne Control Cleanser", "CeraVe", "Cleanser with salicylic acid for acne-prone skin.", "غسول بحمض الساليسيليك للبشرة المعرضة للحبوب.", "Use once or twice daily.", "يستخدم مرة أو مرتين يومياً.", "/static/products/40.png"),

("CeraVe Acne Control Gel", "CeraVe", "Acne treatment gel with AHA and BHA.", "جل لعلاج الحبوب يحتوي على AHA وBHA.", "Apply a thin layer daily.", "توضع طبقة رقيقة يومياً.", "/static/products/41.png"),

("CeraVe Renewing SA Cream", "CeraVe", "Smooths rough and bumpy skin.", "كريم لتنعيم البشرة الخشنة.", "Apply daily.", "يوضع يومياً.", "/static/products/42.png"),

("CeraVe Skin Renewing Night Cream", "CeraVe", "Night cream for smoother skin.", "كريم ليلي لتجديد البشرة.", "Apply every night.", "يوضع كل ليلة.", "/static/products/43.png"),

("CeraVe Vitamin C Serum", "CeraVe", "Brightening vitamin C serum.", "سيروم فيتامين C لإشراق البشرة.", "Apply in the morning.", "يوضع صباحاً.", "/static/products/44.png"),

("CeraVe Resurfacing Retinol Serum", "CeraVe", "Retinol serum for smoother skin.", "سيروم ريتينول لتنعيم البشرة.", "Use at night.", "يستخدم ليلاً.", "/static/products/45.png"),

("CeraVe Hydrating Cream-to-Foam Cleanser", "CeraVe", "Cream cleanser that transforms into foam.", "غسول كريمي يتحول إلى رغوة.", "Massage then rinse.", "يدلك ثم يغسل.", "/static/products/46.png"),

("CeraVe Moisturizing Lotion SPF50", "CeraVe", "Daily moisturizer with high sun protection.", "مرطب يومي مع حماية عالية من الشمس.", "Apply before sun exposure.", "يوضع قبل التعرض للشمس.", "/static/products/47.png"),

("CeraVe Baby Wash & Shampoo", "CeraVe", "Gentle cleanser for babies.", "غسول وشامبو لطيف للأطفال.", "Use during bath.", "يستخدم أثناء الاستحمام.", "/static/products/48.png"),

("CeraVe Baby Moisturizing Lotion", "CeraVe", "Moisturizing lotion for baby's skin.", "لوشن مرطب لبشرة الأطفال.", "Apply after bath.", "يوضع بعد الاستحمام.", "/static/products/49.png"),

("CeraVe Hydrating Toner", "CeraVe", "Alcohol-free toner that hydrates the skin.", "تونر مرطب خالٍ من الكحول.", "Apply with a cotton pad after cleansing.", "يوضع بقطنة بعد تنظيف البشرة.", "/static/products/50.png"),

("CeraVe Hydrating Mineral Sunscreen SPF50", "CeraVe", "Mineral sunscreen for face.", "واقي شمس معدني للوجه.", "Apply 15 minutes before sun exposure.", "يوضع قبل التعرض للشمس بـ15 دقيقة.", "/static/products/51.png"),

("CeraVe Ultra-Light Moisturizing Gel", "CeraVe", "Lightweight gel moisturizer.", "جل مرطب خفيف.", "Apply daily.", "يوضع يومياً.", "/static/products/52.png"),

("CeraVe Intensive Moisturizing Lotion", "CeraVe", "Long-lasting hydration for dry skin.", "لوشن ترطيب مكثف للبشرة الجافة.", "Apply as needed.", "يوضع عند الحاجة.", "/static/products/53.png"),

("CeraVe Advanced Repair Ointment", "CeraVe", "Protects and repairs dry, cracked skin.", "مرهم لإصلاح البشرة الجافة والمتشققة.", "Apply to affected areas.", "يوضع على المناطق المتضررة.", "/static/products/54.png"),

("CeraVe Comforting Eye Makeup Remover", "CeraVe", "Gentle eye makeup remover.", "مزيل مكياج لطيف للعين.", "Apply with a cotton pad.", "يوضع بقطنة.", "/static/products/55.png"),

("CeraVe Therapeutic Hand Cream", "CeraVe", "Moisturizing hand cream.", "كريم مرطب لليدين.", "Apply after washing hands.", "يوضع بعد غسل اليدين.", "/static/products/56.png"),

("CeraVe Diabetics' Dry Skin Relief", "CeraVe", "Moisturizer for very dry skin.", "مرطب للبشرة شديدة الجفاف.", "Apply twice daily.", "يوضع مرتين يومياً.", "/static/products/57.png"),

("CeraVe Itch Relief Moisturizing Cream", "CeraVe", "Relieves itchy dry skin.", "كريم لتخفيف الحكة وجفاف البشرة.", "Apply to affected area.", "يوضع على المنطقة المصابة.", "/static/products/58.png"),

("CeraVe Facial Moisturizing Lotion SPF50", "CeraVe", "Daily facial moisturizer with SPF50.", "مرطب يومي للوجه مع SPF50.", "Apply every morning before sun exposure.", "يوضع كل صباح قبل التعرض للشمس.", "/static/products/59.png"),

("Ducray Anaphase+ Shampoo", "Ducray", "Strengthening shampoo for weak hair.", "شامبو مقوي للشعر الضعيف.", "Massage into wet hair then rinse.", "يدلك على الشعر المبلل ثم يغسل.", "/static/products/60.png"),

("Ducray Kelual DS Shampoo", "Ducray", "Anti-dandruff shampoo for severe dandruff.", "شامبو مضاد للقشرة الشديدة.", "Use 2-3 times per week.", "يستخدم مرتين إلى ثلاث مرات أسبوعياً.", "/static/products/61.png"),

("Ducray Extra Gentle Shampoo", "Ducray", "Gentle shampoo for daily use.", "شامبو لطيف للاستخدام اليومي.", "Massage then rinse well.", "يدلك ثم يغسل جيداً.", "/static/products/62.png"),

("Ducray Elution Shampoo", "Ducray", "Balancing shampoo for sensitive scalp.", "شامبو متوازن لفروة الرأس الحساسة.", "Apply to wet hair and rinse.", "يوضع على الشعر المبلل ثم يغسل.", "/static/products/63.png"),

("Ducray Sensinol Shampoo", "Ducray", "Soothing shampoo for itchy scalp.", "شامبو مهدئ لفروة الرأس الحساسة.", "Use as needed.", "يستخدم عند الحاجة.", "/static/products/64.png"),

("Ducray Squanorm Shampoo", "Ducray", "Shampoo for oily dandruff.", "شامبو للقشرة الدهنية.", "Use twice weekly.", "يستخدم مرتين أسبوعياً.", "/static/products/65.png"),

("Ducray Dexyane Cream", "Ducray", "Cream for dry and irritated skin.", "كريم للبشرة الجافة والمتهيجة.", "Apply once or twice daily.", "يوضع مرة أو مرتين يومياً.", "/static/products/66.png"),
("Ducray Dexyane Balm", "Ducray", "Nourishing balm for very dry skin.", "بلسم مغذٍ للبشرة شديدة الجفاف.", "Apply generously.", "يوضع بكمية مناسبة.", "/static/products/67.png"),

("Ducray Keracnyl Gel", "Ducray", "Purifying cleansing gel for oily skin.", "جل منظف للبشرة الدهنية.", "Use morning and evening.", "يستخدم صباحاً ومساءً.", "/static/products/68.png"),

("Ducray Keracnyl PP+ Cream", "Ducray", "Cream for acne-prone skin.", "كريم للبشرة المعرضة للحبوب.", "Apply after cleansing.", "يوضع بعد تنظيف البشرة.", "/static/products/69.png"),

("Ducray Melascreen SPF50+", "Ducray", "High protection sunscreen for sensitive skin.", "واقي شمس عالي الحماية للبشرة الحساسة.", "Apply before sun exposure.", "يوضع قبل التعرض للشمس.", "/static/products/70.png"),

("Ducray Melascreen Anti-Spots Serum", "Ducray", "Serum to reduce dark spots.", "سيروم لتقليل البقع الداكنة.", "Apply morning and evening.", "يوضع صباحاً ومساءً.", "/static/products/71.png"),

("Ducray Melascreen Night Cream", "Ducray", "Night cream for brighter skin.", "كريم ليلي لإشراق البشرة.", "Apply every night.", "يوضع كل ليلة.", "/static/products/72.png"),

("Ducray Ictyane Cream", "Ducray", "Daily moisturizing cream.", "كريم مرطب للاستخدام اليومي.", "Apply once daily.", "يوضع مرة يومياً.", "/static/products/73.png"),

("Ducray Ictyane HD Cream", "Ducray", "Cream for very dry skin.", "كريم للبشرة شديدة الجفاف.", "Apply morning and evening.", "يوضع صباحاً ومساءً.", "/static/products/74.png"),

("Ducray Hidrosis Control Roll-On", "Ducray", "Roll-on for excessive sweating.", "رول أون للتعرق الزائد.", "Apply to clean dry skin.", "يوضع على بشرة نظيفة وجافة.", "/static/products/75.png"),

("Ducray Hidrosis Control Cream", "Ducray", "Cream to reduce sweating.", "كريم للتخفيف من التعرق.", "Apply daily.", "يوضع يومياً.", "/static/products/76.png"),

("Ducray Neoptide Lotion", "Ducray", "Hair loss care lotion.", "لوشن للعناية بتساقط الشعر.", "Apply once daily.", "يوضع مرة يومياً.", "/static/products/77.png"),

("Ducray Creastim Lotion", "Ducray", "Hair growth stimulating lotion.", "لوشن محفز لنمو الشعر.", "Apply to scalp daily.", "يوضع على فروة الرأس يومياً.", "/static/products/78.png"),

("Ducray Sabal Shampoo", "Ducray", "Shampoo for oily hair.", "شامبو للشعر الدهني.", "Massage then rinse thoroughly.", "يدلك ثم يغسل جيداً.", "/static/products/79.png"),

("Ducray Kertyol PSO Shampoo", "Ducray", "Shampoo for flaky scalp.", "شامبو لفروة الرأس المتقشرة.", "Use 2-3 times weekly.", "يستخدم مرتين إلى ثلاث مرات أسبوعياً.", "/static/products/80.png"),

("Ducray Kertyol PSO Concentrate", "Ducray", "Concentrate for scaly skin.", "مركز للعناية بالبشرة المتقشرة.", "Apply to affected areas.", "يوضع على المناطق المصابة.", "/static/products/81.png"),

("Ducray Diaseptyl Spray", "Ducray", "Cleansing spray for skin.", "بخاخ لتنظيف البشرة.", "Spray directly onto skin.", "يرش مباشرة على البشرة.", "/static/products/82.png"),

("Ducray Diaseptyl Cream", "Ducray", "Protective skin cream.", "كريم واقٍ للبشرة.", "Apply as needed.", "يوضع عند الحاجة.", "/static/products/83.png"),

("Ducray Keracnyl Repair Cream", "Ducray", "Repair cream for acne treatments.", "كريم مرمم للبشرة أثناء علاج الحبوب.", "Apply after cleansing.", "يوضع بعد تنظيف البشرة.", "/static/products/84.png"),

("Ducray Keracnyl Foaming Gel", "Ducray", "Foaming gel cleanser for oily skin.", "جل رغوي للبشرة الدهنية.", "Massage then rinse.", "يدلك ثم يغسل.", "/static/products/85.png"),

("Ducray Anacaps Reactiv Capsules", "Ducray", "Hair strengthening supplement.", "مكمل غذائي لتقوية الشعر.", "Take as directed.", "يؤخذ حسب الإرشادات.", "/static/products/86.png"),

("Ducray Melascreen Hand Cream", "Ducray", "Hand cream with anti-dark spot care.", "كريم يدين للعناية بالبقع الداكنة.", "Apply daily.", "يوضع يومياً.", "/static/products/87.png"),

("Ducray Ictyane Lip Balm", "Ducray", "Moisturizing lip balm.", "بلسم مرطب للشفاه.", "Apply whenever needed.", "يوضع عند الحاجة.", "/static/products/88.png"),

("Ducray Sensinol Serum", "Ducray", "Soothing serum for sensitive scalp.", "سيروم مهدئ لفروة الرأس الحساسة.", "Apply directly to the scalp.", "يوضع مباشرة على فروة الرأس.", "/static/products/89.png"),

("Palladio Herbal Lipstick", "Palladio", "Herbal lipstick with rich color.", "أحمر شفاه عشبي بلون غني.", "Apply directly to lips.", "يوضع مباشرة على الشفاه.", "/static/products/90.png"),

("Palladio Liquid Foundation", "Palladio", "Lightweight liquid foundation.", "كريم أساس سائل خفيف.", "Apply evenly using a sponge or brush.", "يوزع بالتساوي باستخدام إسفنجة أو فرشاة.", "/static/products/91.png"),

("Palladio Rice Powder", "Palladio", "Oil-absorbing face powder.", "بودرة تمتص الزيوت الزائدة.", "Apply with a powder brush.", "توضع بفرشاة البودرة.", "/static/products/92.png"),

("Palladio Herbal Mascara", "Palladio", "Mascara for longer-looking lashes.", "ماسكارا لرموش تبدو أطول.", "Apply from root to tip.", "توضع من جذور الرموش حتى الأطراف.", "/static/products/93.png"),

("Palladio Brow Pomade", "Palladio", "Creamy eyebrow pomade.", "بوميد كريمي للحواجب.", "Apply with an angled brush.", "يوضع بفرشاة مائلة.", "/static/products/94.png"),

("Palladio Matte Blush", "Palladio", "Matte blush for a natural look.", "أحمر خدود مطفي لإطلالة طبيعية.", "Apply to cheeks with a brush.", "يوضع على الخدود بفرشاة.", "/static/products/95.png"),

("Palladio Herbal Concealer", "Palladio", "Concealer to cover imperfections.", "خافي عيوب لإخفاء الشوائب.", "Blend gently into the skin.", "يدمج بلطف مع البشرة.", "/static/products/96.png"),
("Palladio BB Cream", "Palladio", "BB cream with light coverage.", "كريم BB بتغطية خفيفة.", "Apply evenly over the face.", "يوزع بالتساوي على الوجه.", "/static/products/97.png"),

("Palladio Lip Gloss", "Palladio", "Glossy lip color with shine.", "ملمع شفاه بلمعان جميل.", "Apply directly to lips.", "يوضع مباشرة على الشفاه.", "/static/products/98.png"),

("Palladio Lip Liner", "Palladio", "Lip liner for precise definition.", "قلم تحديد الشفاه.", "Outline lips before lipstick.", "حدد الشفاه قبل وضع أحمر الشفاه.", "/static/products/99.png"),

("Palladio Herbal Eyeshadow Palette", "Palladio", "Eyeshadow palette with natural shades.", "لوحة ظلال عيون بألوان طبيعية.", "Apply with an eyeshadow brush.", "توضع بفرشاة ظلال العيون.", "/static/products/100.png"),

("Palladio Waterproof Eyeliner", "Palladio", "Long-lasting waterproof eyeliner.", "آيلاينر مقاوم للماء.", "Apply along the lash line.", "يوضع على خط الرموش.", "/static/products/101.png"),

("Palladio Precision Eyebrow Pencil", "Palladio", "Eyebrow pencil for natural definition.", "قلم حواجب لتحديد طبيعي.", "Fill in eyebrows with light strokes.", "املأ الحواجب بخطوط خفيفة.", "/static/products/102.png"),

("Palladio Face Primer", "Palladio", "Smooth primer for longer-lasting makeup.", "برايمر لتثبيت المكياج.", "Apply before foundation.", "يوضع قبل كريم الأساس.", "/static/products/103.png"),

("Palladio Makeup Setting Spray", "Palladio", "Keeps makeup fresh all day.", "مثبت مكياج يدوم طوال اليوم.", "Spray after makeup application.", "يرش بعد الانتهاء من المكياج.", "/static/products/104.png"),

("Palladio Highlighter", "Palladio", "Adds a natural glow to the skin.", "هايلايتر يمنح البشرة إشراقة.", "Apply to high points of the face.", "يوضع على أماكن الإضاءة في الوجه.", "/static/products/105.png"),

("Palladio Contour Stick", "Palladio", "Cream contour stick.", "كونتور كريمي.", "Blend after application.", "يدمج بعد التطبيق.", "/static/products/106.png"),

("Palladio Bronzer", "Palladio", "Bronzing powder for a sun-kissed look.", "برونزر لإطلالة برونزية.", "Apply with a large brush.", "يوضع بفرشاة كبيرة.", "/static/products/107.png"),

("Palladio Loose Powder", "Palladio", "Loose powder to set makeup.", "بودرة سائبة لتثبيت المكياج.", "Apply after foundation.", "توضع بعد كريم الأساس.", "/static/products/108.png"),

("Palladio Pressed Powder", "Palladio", "Compact pressed face powder.", "بودرة مضغوطة للوجه.", "Apply with sponge or brush.", "توضع بإسفنجة أو فرشاة.", "/static/products/109.png"),

("Palladio Cream Blush", "Palladio", "Cream blush for a natural glow.", "أحمر خدود كريمي لإشراقة طبيعية.", "Apply with fingertips or sponge.", "يوضع بالأصابع أو الإسفنجة.", "/static/products/110.png"),

("Palladio Herbal Foundation Stick", "Palladio", "Cream foundation stick with buildable coverage.", "فاونديشن كريمي على شكل ستيك.", "Blend evenly over the face.", "يوزع بالتساوي على الوجه.", "/static/products/111.png"),

("Palladio Color Intense Lip Balm", "Palladio", "Moisturizing lip balm with color.", "بلسم شفاه مرطب مع لون.", "Apply directly to lips.", "يوضع مباشرة على الشفاه.", "/static/products/112.png"),

("Palladio Precision Liquid Eyeliner", "Palladio", "Precision liquid eyeliner.", "آيلاينر سائل دقيق.", "Draw a thin line along lashes.", "يرسم خطاً رفيعاً على الرموش.", "/static/products/113.png"),

("Palladio Brow Gel", "Palladio", "Eyebrow styling gel.", "جل لتثبيت الحواجب.", "Brush through eyebrows.", "يمشط على الحواجب.", "/static/products/114.png"),



("Palladio Satin Finish Foundation", "Palladio", "Foundation with satin finish.", "كريم أساس بلمسة ساتان.", "Apply evenly using a brush.", "يوزع بالتساوي بفرشاة.", "/static/products/116.png"),

("Palladio Herbal Compact Powder", "Palladio", "Compact powder for a smooth finish.", "بودرة مضغوطة لملمس ناعم.", "Apply after foundation.", "توضع بعد كريم الأساس.", "/static/products/117.png"),

("Palladio Matte Lip Cream", "Palladio", "Matte liquid lipstick.", "أحمر شفاه سائل مطفي.", "Apply evenly to lips.", "يوضع بالتساوي على الشفاه.", "/static/products/118.png"),

("Palladio Herbal Setting Powder", "Palladio", "Setting powder for long-lasting makeup.", "بودرة تثبيت للمكياج.", "Apply lightly over makeup.", "توضع بخفة فوق المكياج.", "/static/products/119.png"),
 ]
STYLE = """
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}

body{
    background:
    linear-gradient(rgba(246,251,248,.86),rgba(246,251,248,.86)),
    url("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1400");
    background-size:cover;
    background-attachment:fixed;
    background-position:center;
    color:#151515;
}

nav{
    background:rgba(8,124,58,.92);
    backdrop-filter:blur(12px);
    padding:18px 7%;
    display:flex;
    justify-content:space-between;
    align-items:center;
    position:sticky;
    top:0;
    z-index:99;
    box-shadow:0 4px 18px #0003;
}

.logo{
display:flex;
align-items:center;
gap:15px;
font-size:24px;
font-weight:bold;
color:white;
}

nav a{
    color:white;
    text-decoration:none;
    margin:0 10px;
    font-size:16px;
    transition:.3s;
    position:relative;
}

nav a:hover{color:#c9ffd9}

nav a::after{
    content:"";
    position:absolute;
    width:0;
    height:2px;
    background:white;
    bottom:-6px;
    left:0;
    transition:.3s;
}

nav a:hover::after{width:100%}

.translate-btn{
    background:white;
    color:#087c3a;
    padding:8px 15px;
    border-radius:20px;
    border:none;
    cursor:pointer;
    font-weight:bold;
    transition:.3s;
}

.translate-btn:hover{
    background:#111;
    color:white;
}

.hero{
    min-height:88vh;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:60px 20px;
}

.hero-box{
    background:rgba(255,255,255,.45);
    backdrop-filter:blur(15px);
    padding:45px;
    border-radius:35px;
    box-shadow:0 20px 50px #0002;
    animation:up 1s;
}

.hero h1{font-size:58px;color:#087c3a;margin-bottom:15px}
.hero h2{font-size:36px;margin-bottom:20px}

.home-text{
    font-size:25px;
    max-width:850px;
    margin:25px auto;
    line-height:1.9;
    color:#111;
    font-weight:500;
}

.home-list{
    margin-top:35px;
    font-size:25px;
    line-height:2.1;
    color:#111;
}

.btn,button{
    display:inline-block;
    background:#087c3a;
    color:white;
    padding:13px 28px;
    border:none;
    border-radius:30px;
    text-decoration:none;
    cursor:pointer;
    transition:.3s;
    margin:6px;
}

.btn:hover,button:hover{background:#111;transform:translateY(-3px)}

.page{
    padding:55px 7%;
    text-align:center;
    animation:up .8s;
}

.page h1{color:#087c3a;font-size:38px;margin-bottom:10px}

.search{
    width:min(650px,90%);
    padding:15px 20px;
    margin:25px auto;
    border:2px solid #087c3a;
    border-radius:40px;
    font-size:17px;
    display:block;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:25px;
    margin-top:35px;
}

.card{
    background:rgba(255,255,255,.72);
    backdrop-filter:blur(12px);
    padding:22px;
    border-radius:26px;
    box-shadow:0 8px 25px #0002;
    transition:.35s;
    border:1px solid #ffffff88;
}

.card:hover{
    transform:translateY(-10px);
    box-shadow:0 15px 35px #0003;
}

.card img{
    width:100%;
    height:190px;
    object-fit:cover;
    border-radius:20px;
    margin-bottom:15px;
}

.brand{color:#087c3a;font-weight:bold;margin:8px 0}

.box{
    background:rgba(255,255,255,.75);
    backdrop-filter:blur(12px);
    margin:20px auto;
    padding:24px;
    border-radius:22px;
    box-shadow:0 8px 25px #0002;
    max-width:850px;
    text-align:left;
    transition:.3s;
}

.box:hover{transform:scale(1.02)}
.answer{display:none;margin-top:12px;color:#444}
.box:hover .answer{display:block}

.form{
    background:rgba(255,255,255,.75);
    backdrop-filter:blur(14px);
    max-width:400px;
    margin:50px auto;
    padding:35px;
    border-radius:25px;
    box-shadow:0 10px 30px #0002;
    text-align:center;
}

.form input{
    width:100%;
    padding:14px;
    margin:10px 0;
    border:2px solid #087c3a;
    border-radius:25px;
}

.contact-card{
    max-width:650px;
    margin:35px auto;
    font-size:27px;
    line-height:1.9;
}

.contact-card h2{
    font-size:36px;
    color:#087c3a;
}

.big-number{
    font-size:42px;
    font-weight:bold;
    color:#087c3a;
}

.whatsapp-btn{
    font-size:24px;
    background:#25D366;
}

.health-line{
    margin-top:35px;
    font-size:34px;
    color:#087c3a;
    font-weight:bold;
}

.footer{
    background:#111;
    color:white;
    text-align:center;
    padding:25px;
    margin-top:50px;
}

@keyframes up{
    from{opacity:0;transform:translateY(45px)}
    to{opacity:1;transform:translateY(0)}
}

@media(max-width:700px){
    nav{flex-direction:column}
    .links{margin-top:12px;text-align:center}
    .hero h1{font-size:38px}
    .hero h2{font-size:25px}
    .home-text,.home-list{font-size:20px}
}
</style>
"""
NAV = """
<nav>

<div class="logo">

<img src="/static/images/logo.jpg"
alt="IAAT PHARMACY Logo"
style="
width:85px;
height:85px;
border-radius:50%;
object-fit:cover;
transition:.3s;
cursor:pointer;
">

<span style="
color:white;
font-size:30px;
font-weight:700;
margin-left:15px;
letter-spacing:nowrap;
">
IAATPHARM Pharmacy
</span>

</div>
"




</div>

<div class="links">

<a href="/" data-ar="الرئيسية" data-en="Home">
Home
</a>

<a href="/products" data-ar="المنتجات" data-en="Products">
Products
</a>

<a href="/faq" data-ar="الأسئلة الطبية" data-en="Medical FAQ">
Medical FAQ
</a>

<a href="/contact" data-ar="تواصل معنا" data-en="Contact">
Contact
</a>

<a href="/login" data-ar="تسجيل الدخول" data-en="Login">
Login
</a>

<a class="btn"
   href="https://www.moph.gov.lb/en/Drugs/index/3/4848/lebanon-national-drugs-database"
   target="_blank"
   style="
      background:#0b5ed7;
      color:white;
      padding:8px 16px;
      border-radius:20px;
      text-decoration:none;
      font-weight:bold;
      margin-right:10px;
   "
   data-ar="💊 أسعار الأدوية"
   data-en="💊 Drug Prices">
   💊 Drug Prices
</a>
<button class="translate-btn" onclick="translateSite()">
🌍 AR / EN
</button>



</div>

</nav>
"""


TRANSLATE_SCRIPT = """
<script>
let currentLang = localStorage.getItem("lang") || "en";

function applyLang(){
    let elements = document.querySelectorAll("[data-ar][data-en]");
    elements.forEach(el => {
        el.innerHTML = el.getAttribute("data-" + currentLang);
    });

    document.documentElement.lang = currentLang === "ar" ? "ar" : "en";
    document.documentElement.dir = currentLang === "ar" ? "rtl" : "ltr";
}

function translateSite(){
    currentLang = currentLang === "en" ? "ar" : "en";
    localStorage.setItem("lang", currentLang);
    applyLang();
}

window.onload = applyLang;
</script>
"""

def t(ar, en):
    return f'data-ar="{ar}" data-en="{en}"'

def layout(title, content):
    return f"""
    <!DOCTYPE html>
    <html lang="ar">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>{title}</title>
      {STYLE}
    </head>
    <body>
      {NAV}
      {content}
      <div class="footer" data-ar="© 2026 صيدلية ايعات | ايعات - بعلبك | لبنان" data-en="© 2026 IAATPHARM PHARMACY | Iaat - Baalback | Lebanon">
        © 2026 IAATPHARM PHARMACY | Iaat - Baalback | Lebanon
      </div>
      {TRANSLATE_SCRIPT}
    </body>
    </html>
    """
@app.route("/")
def home():
    return layout("IAAT PHARMACY", """
    <section class="hero">
      <div style="text-align:center;animation:up 1s;">

        <h2 style="font-size:34px;color:#111;margin-bottom:5px;"
            data-ar="مرحباً بكم في"
            data-en="Welcome to">
          Welcome to
        </h2>

        <div style="display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;">
               
        <div style="
    display:flex;
    align-items:center;
    justify-content:center;
    gap:25px;
">

    <img src="/static/images/logo.jpg"
     alt="IAATPHARM PHARMACY Logo"
     style="
        width:150px;
        height:150px;
        object-fit:contain;
        border-radius:50%;
        box-shadow:none;
     ">
         

    

</div>
          <h1 style="font-size:70px;color:#087c3a;margin:0;"
              data-ar="صيدلية ايعات"
              data-en="IAATPHARM PHARMACY">
            IAAT PHARMACY
          </h1>
        </div>

        <h2 style="font-size:36px;margin-top:15px;margin-bottom:25px;"
            data-ar="صيدليتكم الموثوقة في ايعات - بعلبك"
            data-en="Your trusted pharmacy in Iaat - Baalback">
          Your trusted pharmacy in Iaat - Baalback
        </h2>

        <p style="font-size:18px;max-width:780px;margin:20px auto;line-height:1.7;color:#111;"
           data-ar="نهتم بصحتكم وجمالكم من خلال توفير منتجات العناية بالبشرة، المكياج، المستحضرات الطبية، والنصائح الصيدلانية الموثوقة."
           data-en="We care about your health and beauty by providing skincare products, makeup, medical products, and trusted pharmacy advice.">
          We care about your health and beauty by providing skincare products, makeup, medical products, and trusted pharmacy advice.
        </p>

        <div style="font-size:18px;line-height:1.9;margin-top:25px;color:#111;">
          <p data-ar="💊 منتجات عناية، مكياج، ومستحضرات طبية"
             data-en="💊 Skincare, makeup, and medical products">
            💊 Skincare, makeup, and medical products
          </p>

          <p data-ar="🩺 نصائح صيدلانية ومعلومات مفيدة"
             data-en="🩺 Pharmacy advice and helpful information">
            🩺 Pharmacy advice and helpful information
          </p>

          <p data-ar="📍 ايعات - بعلبك، لبنان"
             data-en="📍 Iaat - Baalback, Lebanon">
            📍 Iaat - Baalback, Lebanon
          </p>
        </div>

        <br>

        <a class="btn" href="/products"
           data-ar="تصفح المنتجات"
           data-en="Browse Products">
          Browse Products
        </a>

        <a class="btn" href="/contact"
           data-ar="تواصل معنا"
           data-en="Contact Us">
          Contact Us
          
</a>
        </a>

      </div>
    </section>
    """)
   

@app.route("/products")
def products():
    cards = ""
    for name, brand, use_en, use_ar, how_en, how_ar, image in PRODUCTS:
        cards += f"""
        <div class="card">
          <img src="{image}">
          <h2>{name}</h2>
          <p class="brand">{brand}</p>
          <p data-ar="{use_ar}" data-en="{use_en}">{use_en}</p>
          <p>
            <b data-ar="طريقة الاستخدام:" data-en="How to use:">How to use:</b><br>
            <span data-ar="{how_ar}" data-en="{how_en}">{how_en}</span>
          </p>
        </div>
        """

    return layout("Products", f"""
    <div class="page">
      <h1 data-ar="منتجاتنا 💊" data-en="Our Products 💊">Our Products 💊</h1>
      <p data-ar="منتجات عناية بالبشرة، مكياج، ومستحضرات صيدلانية." data-en="Skincare, beauty, makeup and pharmacy care products.">
        Skincare, beauty, makeup and pharmacy care products.
      </p>

      <input class="search" id="search" onkeyup="searchProduct()" placeholder="Search product or brand...">

      <div class="cards">{cards}</div>
    </div>

    <script>
    function searchProduct(){{
      let value = document.getElementById("search").value.toLowerCase();
      let cards = document.getElementsByClassName("card");
      for(let i = 0; i < cards.length; i++){{
        let text = cards[i].innerText.toLowerCase();
        cards[i].style.display = text.includes(value) ? "block" : "none";
      }}
    }}
    </script>
    """)

@app.route("/faq")
def faq():
    return layout("Medical FAQ", """
    <div class="page">
      <h1 data-ar="الأسئلة الطبية الشائعة" data-en="Medical FAQ">Medical FAQ</h1>

      <div class="box">
        <h2 data-ar="1- متى أتناول الدواء؟" data-en="1- When should I take my medicine?">1- When should I take my medicine?</h2>
        <div class="answer" data-ar="يعتمد ذلك على نوع الدواء. اسأل الطبيب أو الصيدلي." data-en="It depends on the medicine. Ask your doctor or pharmacist.">It depends on the medicine. Ask your doctor or pharmacist.</div>
      </div>

      <div class="box">
        <h2 data-ar="2- ماذا أفعل إذا نسيت الجرعة؟" data-en="2- What should I do if I miss a dose?">2- What should I do if I miss a dose?</h2>
        <div class="answer" data-ar="لا تضاعف الجرعة. اسأل الصيدلي عن التصرف الصحيح." data-en="Do not double the dose. Ask the pharmacist what to do.">Do not double the dose. Ask the pharmacist what to do.</div>
      </div>

      <div class="box">
        <h2 data-ar="3- هل يمكن تناول الدواء مع الطعام؟" data-en="3- Can I take medicine with food?">3- Can I take medicine with food?</h2>
        <div class="answer" data-ar="بعض الأدوية تؤخذ مع الطعام وبعضها قبله. اقرأ التعليمات جيداً." data-en="Some medicines are taken with food and others before food. Read the instructions carefully.">Some medicines are taken with food and others before food. Read the instructions carefully.</div>
      </div>

      <div class="box">
        <h2 data-ar="4- كيف أحفظ الأدوية؟" data-en="4- How should I store medicines?">4- How should I store medicines?</h2>
        <div class="answer" data-ar="احفظها في مكان جاف وبعيد عن الشمس والحرارة." data-en="Keep them in a dry place away from sunlight and heat.">Keep them in a dry place away from sunlight and heat.</div>
      </div>

      <div class="box">
        <h2 data-ar="5- هل تنتهي صلاحية الأدوية؟" data-en="5- Do medicines expire?">5- Do medicines expire?</h2>
        <div class="answer" data-ar="نعم، لا تستخدم أي دواء بعد انتهاء تاريخ الصلاحية." data-en="Yes, never use medicine after its expiry date.">Yes, never use medicine after its expiry date.</div>
      </div>

      <div class="box">
        <h2 data-ar="6- هل يمكن مشاركة الدواء مع شخص آخر؟" data-en="6- Can I share my medicine with someone else?">6- Can I share my medicine with someone else?</h2>
        <div class="answer" data-ar="لا، لأن كل شخص يحتاج علاجاً مناسباً لحالته." data-en="No, each person needs treatment suitable for their condition.">No, each person needs treatment suitable for their condition.</div>
      </div>

      <div class="box">
        <h2 data-ar="7- ماذا أفعل عند ظهور حساسية؟" data-en="7- What should I do if I get an allergy?">7- What should I do if I get an allergy?</h2>
        <div class="answer" data-ar="أوقف الدواء وتواصل مع الطبيب فوراً." data-en="Stop the medicine and contact a doctor immediately.">Stop the medicine and contact a doctor immediately.</div>
      </div>

      <div class="box">
        <h2 data-ar="8- كم أشرب ماء مع الدواء؟" data-en="8- How much water should I drink with medicine?">8- How much water should I drink with medicine?</h2>
        <div class="answer" data-ar="يفضل شرب كوب ماء كامل إلا إذا قال الطبيب غير ذلك." data-en="Usually one full glass of water unless your doctor says otherwise.">Usually one full glass of water unless your doctor says otherwise.</div>
      </div>

      <div class="box">
        <h2 data-ar="9- هل المضاد الحيوي يعالج الفيروسات؟" data-en="9- Do antibiotics treat viruses?">9- Do antibiotics treat viruses?</h2>
        <div class="answer" data-ar="لا، المضادات الحيوية تعالج العدوى البكتيرية فقط." data-en="No, antibiotics only treat bacterial infections.">No, antibiotics only treat bacterial infections.</div>
      </div>

      <div class="box">
        <h2 data-ar="10- متى يجب زيارة الطبيب؟" data-en="10- When should I visit a doctor?">10- When should I visit a doctor?</h2>
        <div class="answer" data-ar="إذا استمرت الأعراض أو ازدادت سوءاً أو ظهرت أعراض خطيرة." data-en="If symptoms continue, get worse, or serious symptoms appear.">If symptoms continue, get worse, or serious symptoms appear.</div>
      </div>
    </div>
    """)
@app.route("/contact")
def contact():
    return layout("Contact", """
    
    <section style="
        min-height:85vh;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:60px 20px;
    ">

        <div style="
            width:100%;
            max-width:1000px;
            text-align:center;
        ">

            <!-- Main Title -->
            <h1 style="
                font-size:55px;
                color:#0b5d3b;
                margin-bottom:12px;
                font-weight:800;
            "
            data-en="Get in Touch"
            data-ar="تواصل معنا">
                Get in Touch
            </h1>

            <p style="
                font-size:20px;
                color:#555;
                margin-bottom:45px;
            "
            data-en="Your health and comfort are always our priority."
            data-ar="صحتك وراحتك دائمًا من أولوياتنا.">
                Your health and comfort are always our priority.
            </p>


            <!-- Contact Cards -->
            <div style="
                display:flex;
                justify-content:center;
                align-items:stretch;
                gap:25px;
                flex-wrap:wrap;
                margin-bottom:35px;
            ">


                <!-- LOCATION CARD -->
                <div style="
                    flex:1;
                    min-width:280px;
                    background:rgba(255,255,255,0.92);
                    border-radius:25px;
                    padding:35px 25px;
                    box-shadow:0 12px 35px rgba(0,0,0,0.10);
                    transition:0.3s;
                "
                onmouseover="this.style.transform='translateY(-8px)'"
                onmouseout="this.style.transform='translateY(0)'">

                    <div style="
                        font-size:55px;
                        margin-bottom:15px;
                    ">📍</div>

                    <h2 style="
                        color:#0b5d3b;
                        font-size:28px;
                        margin-bottom:12px;
                    "
                    data-en="Our Location"
                    data-ar="موقعنا">
                        Our Location
                    </h2>

                    <p style="
                        color:#555;
                        font-size:18px;
                        margin-bottom:25px;
                    "
                    data-en="Iaat, Baalbek, Lebanon"
                    data-ar="إيعات، بعلبك، لبنان">
                        Iaat, Baalbek, Lebanon
                    </p>

                    <a href="https://maps.app.goo.gl/vP1uuN49hUq46pUq9"
                       target="_blank"
                       style="
                           display:inline-block;
                           background:#0b5d3b;
                           color:white;
                           padding:13px 25px;
                           border-radius:30px;
                           text-decoration:none;
                           font-size:17px;
                           font-weight:bold;
                           transition:0.3s;
                       "
                       data-en="📍 Open Location"
                       data-ar="📍 افتح الموقع">
                        📍 Open Location
                    </a>

                </div>


                <!-- PHONE CARD -->
                <div style="
                    flex:1;
                    min-width:280px;
                    background:rgba(255,255,255,0.92);
                    border-radius:25px;
                    padding:35px 25px;
                    box-shadow:0 12px 35px rgba(0,0,0,0.10);
                    transition:0.3s;
                "
                onmouseover="this.style.transform='translateY(-8px)'"
                onmouseout="this.style.transform='translateY(0)'">

                    <div style="
                        font-size:55px;
                        margin-bottom:15px;
                    ">📞</div>

                    <h2 style="
                        color:#0b5d3b;
                        font-size:28px;
                        margin-bottom:12px;
                    "
                    data-en="Call Us"
                    data-ar="اتصل بنا">
                        Call Us
                    </h2>

                    <p style="
                        color:#222;
                        font-size:25px;
                        font-weight:bold;
                        margin-bottom:25px;
                    ">
                        +961 76 188 827
                    </p>

                    <a href="tel:YOUR_PHONE_NUMBER"
                       style="
                           display:inline-block;
                           background:#1677ff;
                           color:white;
                           padding:13px 28px;
                           border-radius:30px;
                           text-decoration:none;
                           font-size:17px;
                           font-weight:bold;
                       "
                       data-en="📞 Call Now"
                       data-ar="📞 اتصل الآن">
                        📞 Call Now
                    </a>

                </div>

            </div>


            <!-- WHATSAPP BUTTON -->
            <a href="https://wa.me/YOUR_PHONE_NUMBER"
               target="_blank"
               style="
                   display:inline-flex;
                   align-items:center;
                   justify-content:center;
                   gap:12px;
                   background:#25D366;
                   color:white;
                   padding:17px 38px;
                   border-radius:50px;
                   text-decoration:none;
                   font-size:21px;
                   font-weight:bold;
                   box-shadow:0 10px 30px rgba(37,211,102,0.30);
                   transition:0.3s;
               "
               onmouseover="this.style.transform='scale(1.06)'"
               onmouseout="this.style.transform='scale(1)'"
               data-en="💬 Contact us on WhatsApp"
               data-ar="💬 تواصل معنا عبر واتساب">
                💬 Contact us on WhatsApp
            </a>


            <!-- FINAL MESSAGE -->
            <div style="
                margin-top:55px;
                padding:25px;
            ">

                <h2 style="
                    color:#0b5d3b;
                    font-size:32px;
                    font-weight:800;
                "
                data-en="Your health comes before everything ❤️"
                data-ar="سلامتك أهم من كل شيء ❤️">
                    Your health comes before everything ❤️
                </h2>

            </div>

        </div>

    </section>

    """)
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            message = "تم تسجيل الدخول بنجاح ✅"
        else:
            message = "خطأ في اسم المستخدم أو كلمة المرور ❌"

    return layout("Login", f"""
    <div class="form">
      <h1 data-ar="تسجيل الدخول" data-en="Login">Login</h1>
      <form method="POST">
        <input name="username" placeholder="Username">
        <input name="password" type="password" placeholder="Password">
        <button data-ar="دخول" data-en="Login">Login</button>
      </form>
      <br>
      <a href="/register" data-ar="إنشاء حساب" data-en="Create Account">Create Account</a>
      <p>{message}</p>
    </div>
    """)

@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        users[request.form["username"]] = request.form["password"]
        message = "تم إنشاء الحساب ✅"

    return layout("Register", f"""
    <div class="form">
      <h1 data-ar="إنشاء حساب" data-en="Register">Register</h1>
      <form method="POST">
        <input name="username" placeholder="Username">
        <input name="password" type="password" placeholder="Password">
        <button data-ar="إنشاء الحساب" data-en="Create Account">Create Account</button>
      </form>
      <br>
      <a href="/login" data-ar="الذهاب إلى تسجيل الدخول" data-en="Go to Login">Go to Login</a>
      <p>{message}</p>
    </div>
    """)

if __name__ == "__main__":
    app.run(debug=True)
