import os
import sys
import subprocess
from datetime import datetime
def create_workspace_file(fullPath):
    workspace_file_path = os.path.join(fullPath, 'workspace.code-workspace')
    workspace_content = {
        "folders": [
            {"path": "."}
        ],
        "settings": {},
        "launch": {},
        "files": [
            {"path": "A.cpp", "isOpen": True, "viewColumn": 1},
            {"path": "in.txt", "isOpen": True, "viewColumn": 2},
            {"path": "out.txt", "isOpen": True, "viewColumn": 2}
        ]
    }
    with open(workspace_file_path, 'w') as wf:
        import json
        json.dump(workspace_content, wf, indent=4)
    return workspace_file_path

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
        # Create workspace file
        workspace_file = create_workspace_file(fullPath)
        # Open the workspace in VS Code
        subprocess.run(['code', workspace_file])

    except FileExistsError:
        print("File already exists")
    return fullPath
