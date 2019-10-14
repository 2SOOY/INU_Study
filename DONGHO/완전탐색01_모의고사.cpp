#include <string>
#include <vector>
using namespace std;

int method_1[5] = {1, 2, 3, 4, 5};  //찍는 방식 저장
int method_2[8] = {2, 1, 2, 3, 2, 4, 2, 5};
int method_3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

int score[3];   //맞힌 문제 개수를 카운트

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int student_1 = 0;
    int student_2 = 0;
    int student_3 = 0;
    
    for(int i = 0; i<answers.size(); i++)
    {
        if(student_1 % 5 == 0) student_1 = 0;   //인덱스 접근하기 위함
        if(student_2 % 8 == 0) student_2 = 0;
        if(student_3 % 10 == 0) student_3 = 0;
        
        if(answers[i] == method_1[student_1]) score[0]++;
        if(answers[i] == method_2[student_2]) score[1]++;
        if(answers[i] == method_3[student_3]) score[2]++;
        
        student_1++;
        student_2++;
        student_3++;
    }
    int maxscore = max(score[0], max(score[1], score[2]));  //가장 높은점수 추출
    for(int i = 0; i<3; i++)
    {
        if(maxscore == score[i]) answer.push_back(i+1); //가장 높은점수가 여럿일경우 해당 index push, 0번 인덱스부터 반복문이 돌기때문에 오름차순 정렬은 상관없음
    }
    return answer;
}
