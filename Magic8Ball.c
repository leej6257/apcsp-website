#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[])
{
 if (argc != 2)
  {
    printf("%s : expected 1 args, please enter a question\n", argv[0]);
    return 1;
  }
    char *question = NULL;
    size_t len = 0;
    ssize_t read;
    const char* answers[20] = {
        "It is certain", 
        "It is decidedly so", 
        "Without a doubt",
        "Yes, definitely", 
        "You may rely on it", 
        "As I see it, yes",
        "Most likely", 
        "Outlook good", 
        "Signs point to yes", 
        "Yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now", 
        "Cannot predict now",
        "Concentrate and ask again", 
        "Don't bet on it",
        "My reply is no", 
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    };
    srand(time(NULL));

    question = argv[1];
    
    printf("you asked: %s\n", question);
    printf("\n%s\n", answers[rand() % 20]);

    /*while (1) {
        read = getline(&question, &len, stdin);
        if (read < 2) break;
        printf("\n%s\n", answers[rand() % 20]);
    }*/
//    if (question) free(question);
    return 0;
}
