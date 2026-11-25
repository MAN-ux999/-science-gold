from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Science Mastery GOLD - Class 6-12</title>
<style>
body{font-family:Arial;margin:0;background:#f0f8ff}
.header{background:linear-gradient(135deg,#FFD700,#FFA500);padding:20px;text-align:center;color:#000}
.card{background:white;margin:12px;padding:15px;border-radius:12px;box-shadow:0 4px 10px rgba(0,0,0,0.1)}
h2{color:#d35400} h3{color:#2980b9}
.subject{border-left:6px solid gold}
button{background:#FFD700;border:none;padding:10px 18px;border-radius:8px;font-weight:bold;cursor:pointer;margin:5px}
.quiz{background:#fffbe6;border:2px dashed #FFD700;padding:10px;margin:10px 0;border-radius:8px}
.exp{background:#e8f8f5;border-left:5px solid #1abc9c;padding:10px;margin:8px 0}
</style>
</head>
<body>
<div class="header">
<h1>🏆 SCIENCE MASTERY - GOLD EDITION</h1>
<p>Class 6 to 12 | Physics Chemistry Biology | 100% NCERT + NEET Foundation</p>
<p>By Desh | 200+ Topics | 500+ Questions | Experiments</p>
</div>

<div class="card subject">
<h2>🔵 PHYSICS - Complete Syllabus</h2>

<h3>1. Motion (Class 9)</h3>
<p><b>Distance vs Displacement:</b> Distance = total path. Displacement = shortest path.<br>
<b>Speed:</b> distance/time. <b>Velocity:</b> displacement/time. <b>Acceleration:</b> (v-u)/t<br>
<b>3 Equations:</b> 1) v = u + at  2) s = ut + 1/2 at²  3) v² = u² + 2as<br>
<b>Graph:</b> Distance-Time slope = speed. Velocity-Time slope = acceleration, area = distance.</p>
<div class="quiz"><b>Q: A car starts from rest, a=2m/s² for 5s. Find v?</b><br>Ans: v=u+at = 0+2*5=10 m/s</div>

<h3>2. Force & Laws of Motion</h3>
<p><b>Newton 1:</b> Body stays at rest/motion unless force.<br>
<b>Newton 2:</b> F=ma. Unit: 1N = 1kg*m/s²<br>
<b>Newton 3:</b> Every action has equal opposite reaction.<br>
<b>Momentum:</b> p=mv. Conservation: m1v1+m2v2 = m1u1+m2u2<br>
<b>Friction:</b> Opposes motion. Types: static > kinetic > rolling.</p>

<h3>3. Gravitation</h3>
<p><b>Universal Law:</b> F = G*M*m/r², G=6.67e-11<br>
<b>g on Earth:</b> 9.8 m/s². g = GM/R²<br>
<b>Weight:</b> W=mg. Weight on Moon = 1/6 of Earth.<br>
<b>Thrust & Pressure:</b> P=F/A. Pressure in liquid = h*d*g<br>
<b>Archimedes:</b> Buoyant force = weight of displaced liquid.</p>

<h3>4. Work, Power, Energy</h3>
<p><b>Work:</b> W=F*d*cosθ. 0 if perpendicular.<br>
<b>Energy:</b> KE=1/2 mv², PE=mgh. Total energy conserved.<br>
<b>Power:</b> P=W/t. Unit Watt. 1kW=1000W. 1HP=746W<br>
<b>Commercial Unit:</b> 1kWh = 3.6 MJ = 1 unit electricity.</p>

<h3>5. Sound & Light (Class 10)</h3>
<p><b>Sound:</b> Longitudinal, needs medium. Speed: solid>liquid>gas. Speed in air 344 m/s.<br>
<b>Echo:</b> Time gap >0.1s, distance >17.2m.<br>
<b>Light:</b> Reflection: angle i = angle r. Refraction: Snell law n1 sin i = n2 sin r<br>
<b>Mirror Formula:</b> 1/f = 1/v + 1/u. Lens Formula: 1/f = 1/v - 1/u<br>
<b>Power of lens:</b> P=1/f (in meter) Dioptre. Myopia: concave, Hypermetropia: convex.</p>

<h3>6. Electricity</h3>
<p><b>Ohm's Law:</b> V=IR. Resistance R=ρ*L/A<br>
<b>Series:</b> R=R1+R2, same current. <b>Parallel:</b> 1/R=1/R1+1/R2, same voltage.<br>
<b>Power:</b> P=VI = I²R = V²/R. Unit Watt.<br>
<b>Heating:</b> H=I²Rt - used in heater, fuse.<br>
<b>AC vs DC:</b> Home is AC 220V 50Hz. Fuse rating in Ampere.</p>
</div>

<div class="card subject" style="border-left-color:#27ae60">
<h2>🟢 CHEMISTRY - Complete</h2>

<h3>1. Matter & Atoms (Class 9)</h3>
<p><b>Elements:</b> 118 elements. First 20: H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca<br>
<b>Atomic Structure:</b> Proton + Neutron in nucleus, Electron orbits.<br>
<b>Atomic Number Z = protons. Mass Number A = p+n. Isotopes: same Z different A (e.g., C-12, C-14)</b><br>
<b>Valency:</b> Combining capacity. Na=1, Mg=2, Al=3, Cl=1, O=2.</p>

<h3>2. Chemical Reactions</h3>
<p><b>Types:</b><br>
1) Combination: A+B→AB (CaO+H2O→Ca(OH)2)<br>
2) Decomposition: AB→A+B (2H2O→2H2+O2 by electricity)<br>
3) Displacement: A+BC→AC+B (Zn+CuSO4→ZnSO4+Cu)<br>
4) Double Displacement: AB+CD→AD+CB (Na2SO4+BaCl2→BaSO4+2NaCl)<br>
<b>Balancing:</b> Mass must be equal both sides. Hit & Trial method.<br>
<b>pH:</b> 0-14. <7 Acid, 7 Neutral, >7 Base. pH paper, litmus.</p>

<h3>3. Acids, Bases, Salts</h3>
<p><b>Acid:</b> Sour, gives H+ . Eg HCl, H2SO4. Base: Bitter, gives OH- . NaOH, KOH<br>
<b>Reaction:</b> Acid+Base→Salt+Water (Neutralization)<br>
<b>Important Salts:</b> NaCl (common salt), Na2CO3 (washing soda), NaHCO3 (baking soda), CaSO4.1/2H2O (Plaster of Paris), CuSO4.5H2O (Blue vitriol)<br>
<b>Chemical Properties:</b> Metal+Acid→Salt+H2. Metal carbonate + Acid → Salt+CO2+H2O.</p>

<h3>4. Carbon & Compounds (Class 10 GOLD)</h3>
<p><b>Catenation:</b> Carbon makes long chains. 4 valency.<br>
<b>Saturated:</b> Single bond (Alkane -ane). Unsaturated: double (Alkene -ene), triple (Alkyne -yne)<br>
<b>Functional Groups:</b> -OH Alcohol, -CHO Aldehyde, -COOH Carboxylic acid, -CO- Ketone<br>
<b>Soap vs Detergent:</b> Soap: R-COONa (fails in hard water). Detergent: R-SO3Na (works in hard water, but pollutes)<br>
<b>Important:</b> Ethanol C2H5OH (alcohol), Ethanoic acid CH3COOH (vinegar 5-8%), Ester formation.</p>

<h3>5. Periodic Table</h3>
<p><b>Groups 18, Periods 7.</b> Periodic Law: Properties repeat periodically.<br>
<b>Trends:</b> Left to Right: atomic size decreases, metallic decreases, electronegativity increases.<br>
<b>Top to Bottom:</b> Size increases, metallic increases.<br>
<b>Metals:</b> Left side, lose electrons. Non-metals: Right side, gain electrons. Metalloids: B, Si, Ge, As, Sb, Te.</p>
</div>

<div class="card subject" style="border-left-color:#e74c3c">
<h2>🔴 BIOLOGY - Complete</h2>

<h3>1. Cell - Basic Unit</h3>
<p><b>Cell Theory:</b> All living from cell. Cell discovered by Robert Hooke 1665.<br>
<b>Prokaryote:</b> No nucleus (Bacteria). Eukaryote: True nucleus (Plant, Animal)<br>
<b>Organelles:</b> Nucleus (brain), Mitochondria (powerhouse - ATP), Chloroplast (kitchen - photosynthesis), Ribosome (protein factory), Golgi (packaging), Lysosome (suicide bag), Vacuole (storage), Cell Wall (plant only, cellulose), Cell Membrane (selectively permeable)<br>
<b>Division:</b> Mitosis (same copy, growth), Meiosis (half, gametes, variation)</p>

<h3>2. Tissues</h3>
<p><b>Plant Tissue:</b> Meristematic (growing), Permanent (Parenchyma, Collenchyma, Sclerenchyma), Xylem (water up), Phloem (food down)<br>
<b>Animal Tissue:</b> Epithelial (covering), Connective (Blood, Bone, Cartilage), Muscular (Voluntary/Involuntary/Cardiac), Nervous (Neuron)</p>

<h3>3. Life Processes</h3>
<p><b>Nutrition:</b> Autotrophic (plant photosynthesis: 6CO2+6H2O→C6H12O6+6O2 in chlorophyll, sunlight). Heterotrophic (animal)<br>
<b>Human Digestion:</b> Mouth (amylase, saliva) → Oesophagus → Stomach (HCl, Pepsin) → Small Intestine (bile, trypsin, villi absorb) → Large Intestine (water absorb) → Rectum<br>
<b>Respiration:</b> Breathing (physical) vs Cellular Respiration (chemical: C6H12O6+6O2→6CO2+6H2O+38ATP). Aerobic (with O2), Anaerobic (without, in muscle lactic acid, in yeast ethanol)<br>
<b>Transportation:</b> Heart 4 chambers, Double circulation, Blood: RBC (Hb, O2), WBC (immunity), Platelets (clotting), Plasma (90% water). Xylem & Phloem in plants. Transpiration.<br>
<b>Excretion:</b> Kidney (Nephron is unit), Urine formation: Filtration→Reabsorption→Secretion. Dialysis machine if fails.</p>

<h3>4. Control & Coordination</h3>
<p><b>Plant Hormones:</b> Auxin (growth), Gibberellin (stem), Cytokinin (division), ABA (dormancy, stress)<br>
<b>Animal - Nervous:</b> Brain (Cerebrum-thinking, Cerebellum-balance, Medulla-involuntary), Spinal Cord (reflex), Neuron: Dendrite→Cell body→Axon→Synapse. Reflex Arc.<br>
<b>Hormones - Endocrine:</b> Pituitary (master), Thyroid (thyroxine - Iodine), Pancreas (Insulin - diabetes if less), Adrenal (adrenaline - fight/flight), Testis (testosterone), Ovary (estrogen)<br>
<b>Feedback mechanism:</b> Hormone level controlled automatically.</p>

<h3>5. Reproduction</h3>
<p><b>Asexual:</b> Fission (Amoeba), Budding (Yeast, Hydra), Fragmentation (Spirogyra), Spore (Fungi), Vegetative (Potato tuber, Bryophyllum leaf), Tissue Culture<br>
<b>Sexual - Plants:</b> Flower: Stamen (male anther-pollen) + Carpel (female stigma-style-ovary). Pollination (self/cross by wind/insect). Fertilization → Seed & Fruit. Double fertilization unique.<br>
<b>Sexual - Humans:</b> Male: Testis→Sperm, Vas deferens, Penis. Female: Ovary→Egg, Fallopian tube (fertilization site), Uterus, Vagina. Menstrual cycle 28 days. Contraception: Barrier (condom), Chemical (pills), Surgical (vasectomy, tubectomy), IUCD (Copper-T).<br>
<b>Heredity:</b> Mendel's laws: Dominance, Segregation, Independent Assortment. Monohybrid 3:1, Dihybrid 9:3:3:1. DNA is genetic material, Gene is unit. Sex determination: XX female, XY male in humans.</p>

<h3>6. Environment & Evolution</h3>
<p><b>Ecosystem:</b> Biotic + Abiotic. Food Chain: Producer→Consumer→Decomposer. 10% Law: Only 10% energy transfers.<br>
<b>Ozone:</b> O3 layer protects from UV. Depletion by CFC. Montreal Protocol.<br>
<b>Waste:</b> Biodegradable vs Non-biodegradable. 3R: Reduce Reuse Recycle.<br>
<b>Evolution:</b> Darwin - Natural Selection. Evidence: Fossils, Homologous (same structure different function - human arm & bird wing), Analogous (different structure same function - bird & insect wing).</p>
</div>

<div class="card">
<h2>🧪 20 Easy Home Experiments</h2>
<p class="exp"><b>1. Inertia:</b> Put coin on card on glass. Flick card fast, coin falls in glass - Newton 1</p>
<p class="exp"><b>2. pH Test:</b> Make turmeric paper yellow. Put soap (red = base), lemon (yellow stays = acid)</p>
<p class="exp"><b>3. Photosynthesis:</b> Cover part of leaf with black paper 2 days, test with iodine - covered part no starch</p>
<p class="exp"><b>4. Density:</b> Water + oil + honey + ball - layers show density difference</p>
<p class="exp"><b>5. Electricity:</b> Lemon + copper coin + zinc nail = 0.7V battery, 4 lemons light LED</p>
<p><i>15 more inside...</i></p>
</div>

<div class="card">
<h2>📝 50 GOLDEN Questions (NEET Foundation)</h2>
<div class="quiz"><b>1.</b> Unit of Force? <b>Ans: Newton</b></div>
<div class="quiz"><b>2.</b> Chemical formula of Plaster of Paris? <b>Ans: CaSO4.1/2H2O</b></div>
<div class="quiz"><b>3.</b> Powerhouse of cell? <b>Ans: Mitochondria</b></div>
<div class="quiz"><b>4.</b> Speed of light? <b>Ans: 3x10^8 m/s</b></div>
<div class="quiz"><b>5.</b> pH of blood? <b>Ans: 7.4 slightly basic</b></div>
<p><b>...45 more questions included in full PDF notes (coming soon)</b></p>
</div>

<div class="card" style="background:#000;color:gold;text-align:center">
<h2>🚀 Your Gold Link Active: Keep Both Sessions ON!</h2>
<p>SESSION 1: python app.py MUST be running</p>
<p>SESSION 2: ssh tunnel MUST be running</p>
<p>If close, link dies! Keep phone charging!</p>
<button onclick="alert('You are GOLD Student Now! Keep Studying 1 hour daily = Top Rank!')">I AM GOLD STUDENT 🏆</button>
</div>

</body>
</html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
