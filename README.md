# 🦸 Local IP Management Database API

#### About
<quote>
  This is a local database interaction service in order to save user IP's in an order of your choice. The speed of the return is almost just associated with your deployment server region. By modifying the argument type and usage alongside the database file 
</quote>

### Technologies used
```
FastAPI
Python3
.csv files / DB interacted files
```

### Demo

<div align="center">
	<img src="https://woosal.com/1337/5_ipfastapi.png" />
</div>

### get
- get Ruzgar 
	- `http://localhost:1337/get/ruzgar`
	<img src="https://woosal.com/1337/2_ipfastapi.png" />
- get Paster
	- `http://localhost:1337/get/paster`
	<img src="https://github.com/woosal1337/IP-FastAPI-Management/blob/main/src/1_ipfastapi.png" />

### add
- add Ruzgar
	- `/add/{token}={ip}={userVote}`
	<img src="https://woosal.com/1337/3_ipfastapi.png" />
- add Paster
	- `/add/{token}={ip}={userVote}`
	<img src="https://woosal.com/1337/4_ipfastapi.png" />
	
### If user has already voted before does not matter which artist	
<div align="center">
	<img src="https://woosal.com/1337/6_ipfastapi.png" />
</div>
	
### Notes

This app will be integrated with another project called as [Ses-Sese](https://github.com/woosal1337/Ses-Sese), which is going to be a public voting app and be its backend db.

### License
MIT
