from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pickle
import pandas as pd
with open('model.pckl', 'rb') as fin:
	prophet_model = pickle.load(fin)
def cotton(field):
	input_state = field['state']
	input_district = field['district']
	input_market = field['market']
	input_date = field['date']
	district_dict = {'Anantapur': 11, 'Cuddapah': 41, 'East Godavari': 49, 'Guntur': 62, 'Krishna': 91, 'Kurnool': 93, 'Prakasam': 122, 'Srikakulam': 141, 'Vijayanagaram': 153, 'Visakhapatnam': 156, 'West Godavari': 159, 'Ahmedabad': 1, 'Amreli': 9, 'Banaskanth': 16, 'Bharuch': 22, 'Bhavnagar': 24, 'Gandhinagar': 58, 'Jamnagar': 72, 'Junagarh': 77, 'Kachchh': 78, 'Kheda': 87, 'Mehsana': 102, 'Morbi': 104, 'Narmada': 114, 'Panchmahals': 118, 'Patan': 120, 'Rajkot': 125, 'Sabarkantha': 131, 'Surat': 142, 'Surendranagar': 143, 'Vadodara(Baroda)': 150, 'Bhiwani': 26, 'Faridabad': 51, 'Fatehabad': 53, 'Hissar': 69, 'Jhajar': 74, 'Jind': 75, 'Kaithal': 79, 'Mewat': 103, 'Rohtak': 130, 'Sirsa': 137, 'Bagalkot': 15, 'Belgaum': 19, 'Bellary': 20, 'Bijapur': 27, 'Chamrajnagar': 33, 'Chikmagalur': 36, 'Chitradurga': 37, 'Davangere': 42, 'Dharwad': 46, 'Gadag': 55, 'Gulbarga': 61, 'Hassan': 65, 'Haveri': 67, 'Karwar(Uttar Kannad)': 83, 'Kolar': 88, 'Koppal': 89, 'Mandya': 98, 'Mysore': 106, 'Raichur': 124, 'Shimoga': 135, 'Alirajpur': 6, 'Badwani': 14, 'Burhanpur': 32, 'Chhindwara': 35, 'Dewas': 43, 'Dhar': 44, 'Harda': 64, 'Jhabua': 73, 'Khandwa': 85, 'Khargone': 86, 'Ratlam': 128, 'Ahmednagar': 2, 'Akola': 4, 'Amarawati': 8, 'Aurangabad': 13, 'Beed': 18, 'Buldhana': 31, 'Chandrapur': 34, 'Dhule': 47, 'Gadchiroli': 56, 'Hingoli': 68, 'Jalana': 70, 'Jalgaon': 71, 'Nagpur': 109, 'Nanded': 112, 'Nandurbar': 113, 'Parbhani': 119, 'Sangli': 133, 'Wardha': 158, 'Yavatmal': 161, 'South West Khasi Hills': 140, 'West Khasi Hills': 160, 'Bolangir': 29, 'Gajapati': 57, 'Ganjam': 60, 'Kalahandi': 80, 'Koraput': 90, 'Rayagada': 129, 'Pondicherry': 121, 'Barnala': 17, 'Bhatinda': 23, 'Faridkot': 52, 'Fazilka': 54, 'Ludhiana': 94, 'Mansa': 99, 'Muktsar': 105, 'Sangrur': 134, 'Ajmer': 3, 'Alwar': 7, 'Bharatpur': 21, 'Bhilwara': 25, 'Ganganagar': 59, 'Hanumangarh': 63, 'Jodhpur': 76, 'Nagaur': 108, 'Pali': 116, 'Ariyalur': 12, 'Coimbatore': 39, 'Cuddalore': 40, 'Dharmapuri': 45, 'Dindigul': 48, 'Erode': 50, 'Krishnagiri': 92, 'Madurai': 95, 'Nagapattinam': 107, 'Namakkal': 111, 'Ramanathapuram': 126, 'Salem': 132, 'Theni': 145, 'Thirunelveli': 146, 'Thiruvarur': 147, 'Tuticorin': 149, 'Vellore': 152, 'Villupuram': 154, 'Virudhunagar': 155, 'Adilabad': 0, 'Karimnagar': 82, 'Khammam': 84, 'Mahbubnagar': 96, 'Medak': 101, 'Nalgonda': 110, 'Nizamabad': 115, 'Ranga Reddy Dist.': 127, 'Warangal': 157, 'Hathras': 66, 'Tumkur': 148, 'Vashim': 151, 'Karaikal': 81, 'Palwal': 117, 'Pune': 123, 'Sonepur': 139, 'Chittorgarh': 38, 'Aligarh': 5, 'Anand': 10, 'Mahendragarh-Narnaul': 97, 'Bikaner': 28, 'Sikar': 136, 'Sivaganga': 138, 'Thanjavur': 144, 'Mathura': 100, 'Botad': 30}
	state_dict = {'Andhra Pradesh': 0, 'Gujarat': 1, 'Haryana': 2, 'Karnataka': 3, 'Madhya Pradesh': 4, 'Maharashtra': 5, 'Meghalaya': 6, 'Odisha': 7, 'Pondicherry': 8, 'Punjab': 9, 'Rajasthan': 10, 'Tamil Nadu': 11, 'Telangana': 12, 'Uttar Pradesh': 13}
	market_dict={'Gooti': 202, 'Jammalamadugu': 263, 'Kamalapuram': 298, 'Mydukur': 431, 'Proddatur': 509, 'Pithapuram': 503, 'Chilakaluripet': 124, 'Krosuru': 358, 'Macharla': 380, 'Pidugurala(Palnadu)': 500, 'Sattenapalli': 563, 'Tadikonda': 615, 'Vinukonda': 678, 'Jaggayyapeta': 247, 'Kanchekacherla': 302, 'Mylavaram': 432, 'Nandigama': 442, 'Nuzvid': 468, 'Adoni': 5, 'Allagadda': 14, 'Alur': 15, 'Banaganapalli': 49, 'Dhone': 154, 'Koilkunta': 343, 'Yemmiganur': 696, 'Darsi': 136, 'Markapur': 411, 'Martur': 412, 'Parchur': 486, 'Amadalavalasa': 17, 'Hiramandalam': 231, 'Palakonda': 473, 'Pathapatnam': 494, 'Rajam': 518, 'Bobbili': 97, 'Gajapathinagaram': 176, 'Kurupam': 365, 'Parvathipuram': 492, 'Saluru': 549, 'Visakhapatnam': 682, 'Chintalapudi': 127, 'Polavaram': 505, 'Dhandhuka': 146, 'Dholka': 152, 'Dholka(Koth)': 153, 'Ranpur': 534, 'Viramgam': 679, 'Amreli': 22, 'Babra': 38, 'Bagasara': 43, 'Damnagar': 135, 'Dhari': 148, 'Khambha': 326, 'Rajula': 523, 'Savarkundla': 567, 'Amirgadh': 20, 'Deesa(Bhildi)': 141, 'Diyodar': 162, 'Palanpur': 475, 'Amod': 21, 'Hasot': 223, 'Jambusar': 260, 'Jambusar(Kaavi)': 261, 'Jhagadiya': 275, 'Valia': 660, 'Valia(Nethrang)': 661, 'Bhavnagar': 76, 'Botad(Bhabarkot)': 108, 'Botad(Haddad)': 109, 'Gadada': 172, 'Gariyadar': 186, 'Mahuva(Station Road)': 388, 'Palitana': 476, 'Taleja': 616, 'Mansa': 404, 'Bhanvad': 73, 'Dhrol': 156, 'Jam Jodhpur': 257, 'Jam Khambalia': 258, 'Jamnagar': 265, 'Kalawad': 294, 'Lalpur': 370, 'Bhesan': 78, 'Junagadh': 282, 'Kodinar(Dollasa)': 342, 'Manavdar': 399, 'Una': 648, 'Visavadar': 683, 'Anjar': 25, 'K.Mandvi': 284, 'Balasinor': 46, 'Kapadanj(Moti Jaher)': 304, 'Kapadvanj': 305, 'Virpur': 680, 'Becharaji': 64, 'Kadi': 287, 'Kadi(Kadi cotton Yard)': 288, 'Unava': 649, 'Vijapur(Gojjariya)': 673, 'Visnagar': 684, 'Vankaner': 664, 'Rajpipla': 522, 'Gogamba': 194, 'Harij': 221, 'Patan': 493, 'Siddhpur': 589, 'Dhoraji': 155, 'Gondal': 199, 'Jamkandorna': 262, 'Jasdan': 269, 'Jetpur(Dist.Rajkot)': 272, 'Morbi': 425, 'Rajkot': 521, 'Upleta': 650, 'Bayad': 60, 'Bayad(Demai)': 61, 'Bayad(Sadamba)': 62, 'Bhiloda': 82, 'Dhansura': 147, 'Himatnagar': 227, 'Idar': 243, 'Idar(Jadar)': 244, 'Khedbrahma': 334, 'Meghraj': 419, 'Modasa': 422, 'Modasa(Tintoi)': 423, 'Talod': 618, 'Vadali': 653, 'Kosamba(Vankal)': 351, 'Kosamba(Zangvav)': 352, 'Nizar': 464, 'Chotila': 131, 'Halvad': 215, 'Limdi': 374, 'Muli': 427, 'Sayala': 572, 'Vadhvan': 655, 'Bodeli': 98, 'Bodeli(Hadod)': 99, 'Bodeli(Kalediya)': 100, 'Bodeli(Modasar)': 101, 'Jepur Pavi(Chackak)': 271, 'Jetpur-Pavi': 273, 'Karjan': 311, 'Nasvadi': 456, 'Nasvadi(Thalkala)': 457, 'Savli': 568, 'Savli(Desar)': 569, 'Savli(Samlaya)': 570, 'Vagodiya': 657, 'Bhiwani': 83, 'Ch. Dadri': 114, 'Jui': 280, 'Loharu(Dighwa)': 378, 'Siwani': 601, 'Tosham': 643, 'Palwal': 477, 'Bhattu Kalan': 75, 'Fatehabad': 169, 'Jakhal': 253, 'Ratia': 535, 'Tohana': 642, 'Adampur': 3, 'Barwala(Hisar)': 56, 'Hansi': 216, 'Narnaund': 451, 'Uklana': 645, 'Beri': 67, 'Jullana': 281, 'Narwana': 455, 'Pillukhera': 502, 'Uchana': 644, 'Kalayat': 295, 'Hathin': 224, 'Meham': 420, 'Dabwali': 133, 'Ding': 161, 'Ellanabad': 166, 'kalanwali': 700, 'Sirsa': 600, 'Badami': 39, 'Bilagi': 92, 'Hungund': 238, 'Jamakhandi': 259, 'Athani': 36, 'Bailahongal': 45, 'Gokak': 196, 'Kudchi': 361, 'Ramdurga': 528, 'Sankeshwar': 557, 'Soundati': 603, 'Bellary': 65, 'H.B. Halli': 209, 'Hoovinahadagali': 236, 'Kottur': 356, 'Sirguppa': 598, 'Bijapur': 90, 'Sindagi': 592, 'Talikot': 617, 'Chamaraj Nagar': 115, 'Gundlupet': 207, 'Kollegal': 345, 'Bagepalli': 44, 'Kadur': 289, 'Tarikere': 621, 'Chitradurga': 129, 'Davangere': 139, 'Harappana Halli': 220, 'Honnali': 235, 'Annigeri': 26, 'Dharwar': 151, 'Hubli (Amaragol)': 237, 'Kalagategi': 291, 'Kundagol': 364, 'Gadag': 173, 'Laxmeshwar': 373, 'Nargunda': 448, 'Gulburga(Jhevargi)': 206, 'Shorapur': 586, 'Arasikere': 30, 'Belur': 66, 'Haveri': 225, 'Hirekerur': 232, 'Ranebennur': 532, 'Savanur': 566, 'Shiggauv': 582, 'Haliyala': 214, 'Mundgod': 430, 'Yellapur': 694, 'Chintamani': 128, 'Malur': 397, 'Gangavathi': 185, 'Yalburga': 691, 'Nagamangala': 433, 'Srirangapattana': 608, 'Hunsur': 239, 'K.R.Nagar': 286, 'Nanjangud': 445, 'Santhesargur': 558, 'T. Narasipura': 614, 'Lingasugur': 375, 'Manvi': 407, 'Raichur': 516, 'Sindhanur': 593, 'Bhadravathi': 70, 'Shikaripura': 583, 'Shimoga': 584, 'Alirajpur': 13, 'Jobat': 277, 'Anjad': 24, 'Badwani': 42, 'Balwadi': 48, 'Khetia': 335, 'Sendhwa': 576, 'Burhanpur': 112, 'Pandhurna': 480, 'Saunsar': 565, 'Loharda': 376, 'Dhamnod': 145, 'Gandhwani': 180, 'Kukshi': 362, 'Manawar': 400, 'Rajgarh': 520, 'Khirakiya': 336, 'Jhabua': 274, 'Petlawad': 499, 'Thandla': 625, 'Khandwa': 331, 'Pandhana': 479, 'Badwaha': 41, 'Bhikangaon': 79, 'Karhi': 309, 'Kasrawad': 314, 'Khargone': 333, 'Sanawad': 551, 'Segaon': 573, 'Ratlam': 536, 'Sailana': 546, 'Newasa': 461, 'Pathardi': 495, 'Sangamner': 552, 'Shevgaon': 581, 'Shrigonda': 587, 'Shrigonda(Gogargaon)': 588, 'Akot': 10, 'Barshi Takli': 54, 'Telhara': 622, 'Amarawati': 19, 'Chandur Railway': 119, 'Daryapur': 138, 'Dhamngaon-Railway': 144, 'Varud': 666, 'Fulmbri': 171, 'Khultabad': 337, 'Lasur Station': 371, 'Soygaon': 604, 'Vaijpur': 658, 'Gevrai': 187, 'Kille Dharur': 338, 'Majalgaon': 390, 'Vadvani': 656, 'Deoulgaon Raja': 142, 'Khamgaon': 328, 'Chimur': 125, 'Korpana': 350, 'Rajura': 524, 'Varora': 665, 'Shirpur': 585, 'Aheri': 6, 'Akhadabalapur': 8, 'Basmat': 57, 'Hingoli': 229, 'Jawala-Bajar': 270, 'Kalamnuri': 293, 'Bhokardan': 86, 'Ghansawangi': 189, 'Jalana': 254, 'Jalna(Badnapur)': 256, 'Mantha': 405, 'Partur': 490, 'Jalgaon': 255, 'Jamner': 266, 'Jamner(Neri)': 267, 'Yawal': 692, 'Bhiwapur': 84, 'Kalmeshwar': 297, 'Katol': 317, 'Mandhal': 402, 'Narkhed': 449, 'Parshiwani': 489, 'Savner': 571, 'Umared': 646, 'Bhokar': 85, 'Hadgaon': 211, 'Hadgaon(Tamsa)': 212, 'Himalyatnagar': 226, 'Kinwat': 340, 'Mahur': 387, 'Naigaon': 437, 'Shahada': 578, 'Gangakhed': 182, 'Jintur': 276, 'Manwat': 408, 'Parbhani': 485, 'Purna': 514, 'Selu': 574, 'Sonpeth': 602, 'Aatpadi': 0, 'Arvi': 33, 'Ashti': 34, 'Hinganghat': 228, 'Pulgaon': 512, 'Samudrapur': 550, 'Sindi': 594, 'Sindi(Selu)': 595, 'Wardha': 688, 'Babhulgaon': 37, 'Darwha': 137, 'Digras': 159, 'Ghatanji': 191, 'Kalamb': 292, 'Mahagaon': 386, 'Maregoan': 410, 'Pandhakawada': 478, 'Ralegaon': 525, 'Umarkhed': 647, 'Vani': 662, 'Yeotmal': 697, 'ZariZamini': 699, 'Mawkyrwat': 415, 'Nongstoin': 467, 'Bolangir(Patnagarh)': 106, 'Kasinagar': 313, 'Parlakhemundi': 488, 'Digapahandi': 158, 'Bhawanipatna': 77, 'Kesinga': 322, 'Koraput': 347, 'Koraput(Semilguda)': 348, 'Gunpur': 208, 'Rayagada': 539, 'Rayagada(Muniguda)': 540, 'Karaikal': 307, 'Madagadipet': 381, 'Thattanchavady': 628, 'Barnala': 53, 'Tapa(Tapa Mandi)': 620, 'Bhucho': 88, 'Maur': 414, 'Raman': 526, 'Rampura Phul': 529, 'Rampuraphul(Nabha Mandi)': 530, 'Sangat': 553, 'Faridkot': 168, 'Jaitu': 252, 'Kotkapura': 355, 'Abohar': 1, 'Fazilka': 170, 'Jagraon': 248, 'Bareta': 51, 'Bhikhi': 80, 'Boha': 105, 'Budalada': 110, 'Sardulgarh': 560, 'Bariwala': 52, 'Giddarbaha': 192, 'Malout': 394, 'Muktsar': 426, 'Ahmedgarh': 7, 'Dhuri': 157, 'Sangrur': 555, 'Sunam': 611, 'Beawar': 63, 'Bijay Nagar': 91, 'Kekri': 319, 'Vijay Nagar(Gulabpura)': 674, 'Alwar': 16, 'Khairthal': 324, 'Nagar': 435, 'Gangapur': 183, 'Anoopgarh': 28, 'Gajsinghpur': 177, 'Gharsana': 190, 'Jaitsar': 251, 'Kesarisinghpur': 321, 'Lalgarh Jatan': 369, 'Padampur': 471, 'Raisingh Nagar': 517, 'Rawla': 538, 'Sadulshahar': 545, 'Sri Karanpur': 605, 'Sri Vijayanagar': 606, 'Sriganganagar': 607, 'Bhadara': 68, 'Goluwala': 198, 'Hanumangarh': 217, 'Hanumangarh Town': 218, 'Hanumangarh(Urlivas)': 219, 'Nohar': 465, 'Pilli Banga': 501, 'Rawatsar': 537, 'Sangriya': 554, 'Suratgarh': 613, 'Bilara': 93, 'Mathania': 413, 'Merta City': 421, 'Rani': 533, 'Sumerpur': 610, 'Ariyalur Market': 31, 'Annur': 27, 'Pethappampatti': 498, 'Panruti': 481, 'Papparapatti': 483, 'Dindigul': 160, 'Natham': 458, 'Oddunchairum': 469, 'Vadamadurai': 654, 'Vedachandur': 668, 'Anthiyur': 29, 'Boothapadi': 107, 'Moolanur': 424, 'Sathyamangalam': 562, 'Uthangarai': 652, 'Thirumangalam': 631, 'Usilampatty': 651, 'Kuttulam': 367, 'Mailaduthurai': 389, 'Nagapattinam': 434, 'Sembanarkoil': 575, 'Sirkali': 599, 'Namakkal': 440, 'Paramakudi': 484, 'Gangavalli': 184, 'Karumanturai': 312, 'Kolathur': 344, 'Konganapuram': 346, 'Thalaivasal': 623, 'Vazhapadi': 667, 'Theni': 629, 'Sankarankovil': 556, 'Tirunelvali': 639, 'Kudavasal': 360, 'Thiruvarur': 635, 'Valangaiman': 659, 'Kovilpatti': 357, 'Gudiyatham': 205, 'Gingee': 193, 'Thirukovilur': 630, 'Tindivanam': 637, 'Vikkiravandi': 676, 'Villupuram': 677, 'Rajapalayam': 519, 'Virudhunagar': 681, 'Adilabad': 4, 'Asifabad': 35, 'Bhainsa': 72, 'Boath': 96, 'Chinnoar': 126, 'Ichoda': 242, 'Indravelly(Utnoor)': 245, 'Jainath': 249, 'Jainoor': 250, 'Kagaznagar': 290, 'Khanapur': 330, 'Kuber': 359, 'Laxettipet': 372, 'Mancharial': 401, 'Nirmal': 463, 'Sarangapur': 559, 'Choppadandi': 130, 'Dharmaram': 149, 'Gangadhara': 181, 'Gollapally': 197, 'Husnabad': 240, 'Jammikunta': 264, 'Karimnagar': 310, 'Kataram': 315, 'Mallial(Cheppial)': 393, 'Manthani': 406, 'Peddapalli': 496, 'Pudur': 511, 'Sircilla': 597, 'Sultanabad': 609, 'Vemulawada': 670, 'Bhadrachalam': 69, 'Burgampadu': 111, 'Charla': 121, 'Dammapet': 134, 'Enkoor': 167, 'Kallur': 296, 'Khammam': 329, 'Kothagudem': 354, 'Madhira': 382, 'Nelakondapally': 460, 'Sattupalli': 564, 'Wyra': 690, 'Yellandu': 693, 'Amangal': 18, 'Badepalli': 40, 'Makthal': 391, 'Narayanpet': 447, 'Shadnagar': 577, 'Dubbak': 165, 'Gajwel': 178, 'Jogipet': 279, 'Medak': 416, 'Narayankhed': 446, 'Narsapur': 454, 'Ramayampet': 527, 'Siddipet': 590, 'Togguta': 641, 'Zaheerabad': 698, 'Aler': 11, 'Chandur': 118, 'Chandur(Mungodu)': 120, 'Choutuppal': 132, 'Halia': 213, 'Nakrekal': 438, 'Venkateswarnagar': 671, 'Venkateswarnagar(Chintapalli)': 672, 'Armoor': 32, 'Banswada': 50, 'Bichkunda': 89, 'Bodhan': 102, 'Gandhari': 179, 'Kamareddy': 299, 'Kammarpally': 300, 'Madnoor': 384, 'Pitlam': 504, 'Yellareddy': 695, 'Marapally': 409, 'Medchal': 417, 'Vikarabad': 675, 'Cherial': 122, 'Dornakal': 164, 'Ghanpur': 188, 'Jangaon': 268, 'Kesamudram': 320, 'Kodakandal': 341, 'Mahabubabad': 385, 'Mulugu': 429, 'Narsampet': 452, 'Narsampet(Nekonda)': 453, 'Parkal': 487, 'Thorrur': 636, 'Warangal': 687, 'Wardhannapet': 689, 'Haathras': 210, 'Peddapuram': 497, 'Ponduru': 507, 'Malpur': 396, 'Nippani': 462, 'Rona': 542, 'Byadagi': 113, 'Devadurga': 143, 'Sira': 596, 'Dharni': 150, 'Tiwasa': 640, 'Kannad': 303, 'Sillod': 591, 'Chikali': 123, 'Malkapur': 392, 'Bhadrawati': 71, 'Chandrapur': 116, 'Dondaicha': 163, 'Navapur': 459, 'Mangrulpeer': 403, 'Goniana': 201, 'Pudupalayam': 510, 'Gopalpatti': 203, 'Tiruchengode': 638, 'Omalur': 470, 'Poonthottam': 508, 'Kathalapur': 316, 'Koratla': 349, 'Gadwal': 174, 'Gadwal(Lezza)': 175, 'Sadasivpet': 544, 'Bhiknoor': 81, 'Sadashivnagar': 543, 'Hodal': 234, 'K.R. Pet': 285, 'Sakri': 547, 'Hingoli(Kanegoan Naka)': 230, 'Partur(Vatur)': 491, 'Bodwad': 104, 'Nanded': 441, 'Mulshi': 428, 'Birmaharajpur': 95, 'Kapasan': 306, 'Kavunthapadi': 318, 'Thirupathur': 632, 'Wanaparthy Road': 685, 'Wanaparthy Road(Prbbair)': 686, 'Birkur': 94, 'Velpur': 669, 'Aligarh': 12, 'Khair': 323, 'Khambhat': 327, 'Deesa': 140, 'Lakhani': 368, 'Baruch(Vagara)': 55, 'Gogamba(Similiya)': 195, 'Talod(Harsol)': 619, 'Loharu': 377, 'Ballabhgarh': 47, 'Hissar': 233, 'Khanina': 332, 'Narnaul': 450, 'Shahapur': 579, 'Harsood': 222, 'Chandrapur(Ganjwad)': 117, 'Gondpimpri': 200, 'Nagpur(Hingna)': 436, 'Ramtek': 531, 'Nandurbar': 444, 'Bathinda': 59, 'Khajuwala': 325, 'Lunkaransar': 379, 'Nokha': 466, 'Ridmalsar': 541, 'Jodhpur(Grain)(Phalodi)': 278, 'Surajgarh': 612, 'Karamadai': 308, 'Thiruppur': 634, 'Namagiripettai': 439, 'Kamuthi': 301, 'Salem': 548, 'Thammampati': 624, 'Manamadurai': 398, 'Kumbakonam': 363, 'Papanasam': 482, 'Thiruppananthal': 633, 'Bodinayakkanur': 103, 'Vaniyambadi': 663, 'Sathur': 561, 'Gopalraopet': 204, 'Huzzurabad': 241, 'Medipally': 418, 'Kosikalan': 353, 'Junagarh': 283, 'Pollachi': 506, 'Palani': 474, 'Bhongir': 87, 'Thara': 626, 'Thara(Shihori)': 627, 'Bharuch': 74, 'Jagalur': 246, 'Kustagi': 366, 'Madhugiri': 383, 'Akola': 9, 'Achalpur': 2, 'Anajngaon': 23, 'Paithan': 472, 'Nandura': 443, 'Shegaon': 580, 'Basmat(Kurunda)': 58, 'Pusad': 515, 'Malout (Kilianwali)': 395, 'Punchaipuliyampatti': 513, 'Kilvelur': 339}
	ds=input_date
	State_Code = state_dict[input_state]
	District_Code = district_dict[input_district]
	Market_Code = market_dict[input_market]
	#ds = pd.to_datetime(ds)
	input_data=[[ds, State_Code, District_Code, Market_Code]]
	df_pred = pd.DataFrame(input_data, columns = ['ds', 'State_Code', 'District_Code', 'Market_Code'])
	#converting df columns to category dtype
	df_pred['State_Code'] = df_pred.State_Code.astype('category')
	df_pred['District_Code'] = df_pred.District_Code.astype('category')
	df_pred['Market_Code'] = df_pred.Market_Code.astype('category')
	pred_result = prophet_model.predict(df_pred)
	result=pred_result
	Row_list =[]
	for index, rows in result.iterrows():Row_list.append(rows.yhat)
	return str(Row_list[0])
result=cotton({'state': "Andhra Pradesh", 'district': "Anantapur", 'market': "Gooti", 'date': '2015-03-15'})



##############################################################################################################################################################################



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts1.db'
db = SQLAlchemy(app)

class listofcust(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gmail = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100), nullable=False)
    district = db.Column(db.Text, nullable=False)
    market = db.Column(db.String(20), nullable=False, default='N/A')
    state=db.Column(db.String(20), nullable=False, default='N/A')
   

    def __repr__(self):
        return 'cutomer' + str(self.id)
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/printpredict')
def printpredict():
    if request.method=='GET':
         return render_template('printpredict.html')
        

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
      if request.method == 'POST':
        post_state = request.form['state']
        post_district = request.form['district']
        post_market = request.form['market']
        post_date=request.form['date']
        
        all_post={'state': post_state,
                   'district' :post_district,
                    'market':post_market,
                       'date' :post_date,
                  
                  }
        value=cotton(all_post)
        all_post['price']=value
        return render_template('printpredict.html',post=all_post)
      else:
        return render_template('prediction.html')
'''@app.route('/login')
def index2():
    if request.method == 'POST':
        post_email= request.form['email']
        post_pwd = request.form['pwd']
        user=listofcust.query.filter_by(gmail=post_gmail).first()
        if user is None or user.password!=post_password:
            return redirect('/login')
        else:
            post_gmail = user.gmail
            post_password = user.password
            post_district = user.district
            post_market = user.market
            post_state = user.state
            all_posts={"gmail":user.gmail,
                       "password":user.password,
                        "district" :user.district,
                        "market" :user.market,
                        "state" : user.state
                }
            return render_template('index2.html',posts=all_posts)
    else:
      return render_template('signin.html')'''
    
'''@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        post_gmail = request.form['gmail']
        post_password = request.form['password']
        post_district = request.form['district']
        post_market = request.form['market']
        post_state = request.form['state']
        new_post = listofcust(gmail =post_gmail ,password =post_password ,district =  post_district ,market=post_market,state=post_state)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/login')'''


  
        
        

    
if __name__ == "__main__":
    app.run(debug=True)
