# Average_Salary_SMPC

## Server
### Step 1. Clone MP-SPDZ
Clone a copy of the main git repository of MP-SPDZ
```
git clone https://github.com/data61/MP-SPDZ.git
make setup
make -j 8 all
```
 詳情請見[此處](https://github.com/data61/MP-SPDZ#readme)
### Step 2. Clone Average_Salary_SMPC
 Clone a copy of the main git repository of Average_Salary_SMPC
```
git clone https://github.com/B08902060/Average_Salary_SMPC
```
### Step 3. Cope Files
```
cp Average_Salary_SMPC/Programs/Source/average_gender_salary.mpc MP-SPDZ/Programs/Source
``` 
### Step 4. 
```
cd MP-SPDZ/
./compile.py average_gender_salary 1
Scripts/setup-ssl.sh <nparties>
Scripts/setup-clients.sh <clients_number>
====分發SSL證書====
./proctol.x <party_number> average_gender_salary-1 -mp <my_port_number> -N <parties_number> -h <Party0_IP> -pn <Party0_port_number>
``` 
## Client
### Step 1. Istall gmpy2
 ```
pip install gmpy2
```
### Step 2. Clone Average_Salary_SMPC
 Clone a copy of the main git repository of Average_Salary_SMPC
```
git clone https://github.com/B08902060/Average_Salary_SMPC
```
### Step 3. Set Certificate
```
mkdir Player-Data
cd Player-Data/
===寫入接收的SSL證書===
cd ../
``` 
### Step 4. Run Protocol
```
python3 ./PATH/average_salary.py <n_parties> <finish> <party_0_port number> <ip_party_0> <ip_party_1> ... <ip_party_(n-1)> 
``` 
