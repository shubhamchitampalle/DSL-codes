#include <iostream>
#define size 10
using namespace std;
class cqueue
{
    int f = -1, r = -1;
    int q[size];
public:
    int isfull()
    {
        if (f == r + 1)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    int isempty()
    {
        if (r == f)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    void enqueue()
    {
        if (isfull() == 1)
        {
            cout << "queue is overflow "<<endl;
        }
        else
        {
            if (f == -1)
            {
                f++;
                r++;
            }
            cout << "enter value ";
            cin >> q[r];
            r = (r + 1) % 10;
        }
    }
    void dequeue()
    {
        if (isempty() == 1)
        {
            cout << "queue is underflow " << endl;
        }
        else
        {
            cout << "deleted value " << q[f]<<endl;
            f = (f + 1) % 10;
        }
    }
    void display()
    {
        for (int i = f; i < r; i++)
        {
            cout << q[i] << " ";
        }
        cout << endl;
    }
};
int main()
{
    cqueue a;
    int ch;
    char c;
    cout << " 1)add orders \n 2)serve orders \n 3)display\n";
    do
    {
        cout << "enter your choice : ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            a.enqueue();
            break;
        case 2:
            a.dequeue();
            break;
        case 3:
            a.display();
            break;
        }
        cout << "do you want to continue y/n: ";
        cin >> c;
    } while (c == 'y');
    return 0;
}