#include <string>
#include <vector>
#include <queue>

using namespace std;
int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
    int answer = 0;
    int day_cnt = 0;
    priority_queue<int, vector<int>> pq;    //최소한의 공급을 위해 재고가 0이 아닌경우 밀가루 공급 수량을 우선순위큐에 넣어 부족할때는 큰순으로 공급받기 위함

    for(int i = 0; i<k; i++)
    {
        if(dates[day_cnt] == i)
        {
            pq.push(supplies[day_cnt]);
            day_cnt++;
        }
        
        if(stock == 0)
        {
            stock += pq.top();  //가장 큰것 공급
            pq.pop();
            answer++;
        }
        stock--;
    }
    return answer;
}
