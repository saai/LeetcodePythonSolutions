bool matchFirst(char *s, char* p){
    return (*s!='\0' && *p == '.') ||(*s==*p);
}

bool isMatch(char* s, char* p) {
    if (*p=='\0') return *s == '\0'; // empty
    if (*(p+1) != '*')
    { // without *
        if (!matchFirst(s,p)) return false;
        return isMatch(s+1,p+1);
    }
    else // with *
    {
        if (isMatch(s,p+2)) return true; // try number 0
        while(matchFirst(s,p)) // try all the possible lengthes
        {
            if (isMatch(++s,p+2)) return true;
        }
        return false;
    }
}

