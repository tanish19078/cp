#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;
    vector<long long> A(N);
    map<long long, int> freq;
    long long total = 0;
    
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        freq[A[i]]++;
        total += A[i];
    }
    
    vector<long long> answers;
    
    // Iterate divisors of total
    for (long long L = 1; L * L <= total; L++) {
        if (total % L != 0) continue;
        
        // Check L
        long long u_plus_b = total / L; // total original sticks
        long long b = N - u_plus_b;
        
        if (b >= 0 && b <= N && (total - b * L) >= 0) {
            long long u = u_plus_b - b; // unbroken sticks
            if (u < 0) continue;

            if (freq[L] < u) continue;

            map<long long, int> remaining = freq;
            remaining[L] -= u;
            
            bool possible = true;
            long long broken_formed = 0;
            
            // Try to pair
            for (auto it = remaining.begin(); it != remaining.end(); ++it) {
                long long x = it->first;
                if (x > L) break; // since x + y = L, x < L
                
                if (x * 2 == L) {
                    // Need even count
                    if (it->second % 2 != 0) {
                        possible = false;
                        break;
                    }
                    broken_formed += it->second / 2;
                    it->second = 0;
                } else {
                    long long y = L - x;
                    if (y <= 0 || y > L) continue;
                    if (remaining.find(y) == remaining.end()) {
                        possible = false;
                        break;
                    }
                    int pairs = min(it->second, remaining[y]);
                    broken_formed += pairs;
                    it->second -= pairs;
                    remaining[y] -= pairs;
                }
            }
            
            if (possible && broken_formed == b) {
                answers.push_back(L);
            }
        }
        

        long long L2 = total / L;
        if (L2 == L) continue;
        
        b = N - L; 
        if (b >= 0 && b <= N && (total - b * L2) >= 0) {
            long long u = L - b;
            if (u < 0) continue;
            
            if (freq[L2] < u) continue;
            
            map<long long, int> remaining = freq;
            remaining[L2] -= u;
            
            bool possible = true;
            long long broken_formed = 0;
            
            for (auto it = remaining.begin(); it != remaining.end(); ++it) {
                long long x = it->first;
                if (x > L2) break;
                
                if (x * 2 == L2) {
                    if (it->second % 2 != 0) {
                        possible = false;
                        break;
                    }
                    broken_formed += it->second / 2;
                    it->second = 0;
                } else {
                    long long y = L2 - x;
                    if (y <= 0 || y > L2) continue;
                    if (remaining.find(y) == remaining.end()) {
                        possible = false;
                        break;
                    }
                    int pairs = min(it->second, remaining[y]);
                    broken_formed += pairs;
                    it->second -= pairs;
                    remaining[y] -= pairs;
                }
            }
            
            if (possible && broken_formed == b) {
                answers.push_back(L2);
            }
        }
    }
    
    sort(answers.begin(), answers.end());
    for (size_t i = 0; i < answers.size(); i++) {
        if (i > 0) cout << " ";
        cout << answers[i];
    }
    cout << "\n";
    
    return 0;
}