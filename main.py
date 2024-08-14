import os
import sys
import subprocess
from datetime import datetime

def create_contest_folder(contestName='Codeforces'):
    basePath='/home/nithin/Codes/CP/Contests/'
    timeStamp=datetime.now().strftime("%b%d-%Y")
    folderName=contestName+"-"+timeStamp
    fullPath=os.path.join(basePath,folderName)
    cppTmpl = '''#include<bits/stdc++.h>
using namespace std;

#define ll long long int
#define vi vector<int>
#define vll vector<long long int>
#define INF INT_MAX
#define MOD 1000000007
#define pii pair<int,int>
#define pb push_back
#define all(x) x.begin(),x.end()
#define clr(x) memset(x,0,sizeof(x))
#define sortUni(v) sort(all(v)), v.erase(unique(all(v)), v.end())
#define fast_io ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define test int t;cin>>t;while(t--)
#define take(a,n) vi a(n); f0(i,n) cin >> a[i];
#define give(a,n) f0(i,n){cout << a[i] << ' ';}cout << endl;

void solve()
{
    
}
int32_t main()
{
    #ifndef ONLINE_JUDGE
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    fast_io;
    test
        solve();
    return 0;
}
'''
    
    try:
        os.makedirs(fullPath)
        print(f"Folder created: {fullPath}")
        files = ['in.txt', 'out.txt', 'A.cpp', 'B.cpp', 'C.cpp', 'D.cpp', 'E.cpp', 'F.cpp']
        for file in files:
            file_path = os.path.join(fullPath, file)
            with open(file_path, 'w') as f:
                if file.endswith('.cpp'):
                    f.write(cppTmpl) 
        subprocess.run(['code', fullPath])

    except FileExistsError:
        print("File already exists")
    return fullPath

def main():
    if len(sys.argv) != 2:
        print("Give the Contest Name!")
        sys.exit(1)
    contestName = sys.argv[1]
    create_contest_folder(contestName)

if __name__ == "__main__":
    main()