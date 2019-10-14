#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    
    priority_queue<int, vector<int>, greater<int>> pq;  //우선순위(작은것이 우선)큐 생성
    for(int i = 0; i<scoville.size(); i++)
    {
        pq.push(scoville[i]);   //우선순위큐에 각 음식 스코빌지수 push
    }
    
    while(pq.top() < K && pq.size() > 1)    //큐의 top이 스코빌지수 K 보다 작고 큐안에 원소가 2개 이상일때동안 반복
    {
        int first_not_spicy = pq.top();
        pq.pop();
        int second_not_spicy = pq.top();
        pq.pop();
        pq.push(first_not_spicy + second_not_spicy * 2);
        answer++;
    }
    if(pq.top() < K) return -1; //K이상으로 만들수 없는 경우
    return answer;
}
