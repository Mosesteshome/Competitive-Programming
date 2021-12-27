class Solution {
public:
    string sortSentence(string s) {
        vector<string>ar(10,"");
        s+=" ";
        string w="";
        int k=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]!=' '&&!isdigit(s[i]))
                w+=s[i];
            else if(isdigit(s[i]))
            {
                ar[s[i]-49]=w;
                w="";
                k++;
            
             }
        }
        s="";
        for(int i=0;i<k;i++)
        {
       
           if(i==k-1)
               s+=ar[i];
            else
                s+=ar[i]+" ";

        }
        return s;
    
    }
};
