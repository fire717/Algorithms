// 16 ms -94%
class Solution {
public:
    bool judgeCircle(string moves) {
        int verticle = 0;
        int horizon = 0;
        int i = 0;
        while( moves[i] != '\0' ){
            if(moves[i] == 'U'){
                verticle += 1;
            }
            else if (moves[i] == 'D'){
                verticle -= 1;
            }
            else if (moves[i] == 'R'){
                horizon += 1;
            }
            else{
                horizon -= 1;
            }
            i++;
        }    
        if(verticle  || horizon ){
            return 0;
        }    
        else{
            return 1;
        }
    }
};
