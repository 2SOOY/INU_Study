#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(int brown, int red) {
	vector<int> answer;

	int sum = brown + red;  //칸당 1이라 생각하고난 후 넓이
	int w = 0, h = 0;
	for (int i = 1; i <= red; i++)
	{
		if (red % i == 0)	//i가 red칸만큼의 높이가 됨
		{
			int w = red / i;    //red칸만큼의 가로 

			if ((w + 2) * (i + 2) == sum)    //red칸만큼의 가로 + 2, 세로 + 2는 넓이, (겉 테두리만 brown이기 때문)
			{
				answer.push_back(w + 2);
				answer.push_back(i + 2);
				break;
			}
		}
	}
	return answer;
}
