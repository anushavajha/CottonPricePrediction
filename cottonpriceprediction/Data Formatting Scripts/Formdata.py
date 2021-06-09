

row = []

days = [0]*31
months = [0]*12
years = [0]*6
states = [0]*14
districts = [0]*163

#13,01,2020,Uttar Pradesh,Hathras,Haathras,5600

day = 30
month = 'January'
year = '2018'
state = 'Uttar Pradesh'
district = 'Aligarh'

months_list = ['January','February','March','April','June','July','August','September','October','November','December']

years_list = ['2015','2016','2017','2018','2019','2020']

states_list = ['Andhra Pradesh', 'Gujarat', 'Haryana', 'Karnataka', 'Madhya Pradesh', 
'Maharashtra', 'Meghalaya', 'Odisha', 'Pondicherry', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telangana', 'Uttar Pradesh']

districts_list = ['Adilabad', 'Ahmedabad', 'Ahmednagar', 'Ajmer', 'Akola', 'Aligarh', 'Alirajpur', 'Alwar', 'Amarawati', 'Amreli', 'Anand', 
'Anantapur', 'Ariyalur', 'Aurangabad', 'Badwani', 'Bagalkot', 'Banaskanth', 'Barnala', 'Beed', 'Belgaum', 'Bellary', 'Bharatpur', 'Bharuch', 
'Bhatinda', 'Bhavnagar', 'Bhilwara', 'Bhiwani', 'Bijapur', 'Bikaner', 'Bolangir', 'Botad', 'Buldhana', 'Burhanpur', 'Chamrajnagar', 
'Chandrapur', 'Chhindwara', 'Chikmagalur', 'Chitradurga', 'Chittorgarh', 'Coimbatore', 'Cuddalore', 'Cuddapah', 'Davangere', 'Dewas', 
'Dhar', 'Dharmapuri', 'Dharwad', 'Dhule', 'Dindigul', 'East Godavari', 'Erode', 'Faridabad', 'Faridkot', 'Fatehabad', 'Fazilka', 'Gadag', 
'Gadchiroli', 'Gajapati', 'Gandhinagar', 'Ganganagar', 'Ganjam', 'Gulbarga', 'Guntur', 'Hanumangarh', 'Harda', 'Hassan', 'Hathras', 'Haveri', 
'Hingoli', 'Hissar', 'Jalana', 'Jalgaon', 'Jamnagar', 'Jhabua', 'Jhajar', 'Jind', 'Jodhpur', 'Junagarh', 'Kachchh', 'Kaithal', 'Kalahandi', 
'Karaikal', 'Karimnagar', 'Karwar(Uttar Kannad)', 'Khammam', 'Khandwa', 'Khargone', 'Kheda', 'Kolar', 'Koppal', 'Koraput', 'Krishna', 
'Krishnagiri', 'Kurnool', 'Ludhiana', 'Madurai', 'Mahbubnagar', 'Mahendragarh-Narnaul', 'Mandya', 'Mansa', 'Mathura', 'Medak', 'Mehsana', 
'Mewat', 'Morbi', 'Muktsar', 'Mysore', 'Nagapattinam', 'Nagaur', 'Nagpur', 'Nalgonda', 'Namakkal', 'Nanded', 'Nandurbar', 'Narmada', 
'Nizamabad', 'Pali', 'Palwal', 'Panchmahals', 'Parbhani', 'Patan', 'Pondicherry', 'Porbandar', 'Prakasam', 'Pune', 'Raichur', 'Rajkot', 
'Ramanathapuram', 'Ranga Reddy Dist.', 'Ratlam', 'Rayagada', 'Rohtak', 'Sabarkantha', 'Salem', 'Sangli', 'Sangrur', 'Shimoga', 'Sikar', 
'Sirsa', 'Sivaganga', 'Sonepur', 'South West Khasi Hills', 'Srikakulam', 'Surat', 'Surendranagar', 'Thanjavur', 'Theni', 'Thirunelveli', 
'Thiruvarur', 'Tumkur', 'Tuticorin', 'Vadodara(Baroda)', 'Vashim', 'Vellore', 'Vijayanagaram', 'Villupuram', 
'Virudhunagar', 'Visakhapatnam', 'Warangal', 'Wardha', 'West Godavari', 'West Khasi Hills', 'Yavatmal']

days[day-1] = 1
months[months_list.index(month)] = 1
years[years_list.index(year)] = 1
states[states_list.index(state)] = 1
districts[districts_list.index(district)]=1

row = days + months + years + states + districts
print((row))



