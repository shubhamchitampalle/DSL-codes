#include<iostream>
#define size 10
using namespace std;
class dequeue
{
    int f = -1;
    int r = -1;
    int q[size];
public:
    int isfull()
    {
        if (r >= size)
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
        if (f == -1)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    void add_front(int x)
    {
        if (f == -1)
        {
            f++;
            r++;
            q[r] = x;
        }
        else if (f != 0)
        {
            f--;
            q[f] = x;
        }
        else
        {
            cout << "queue is overflow " << endl;
        }
    }
    void add_rear(int x)
    {
        if (f == -1)
        {
            f++;
        }
        r++;
        q[r] = x;
    }
    void delete_front()
    {
        if (isempty() == 1)
        {
            cout << "queue is underflow " << endl;
        }
        else
        {
            cout << "deleted " << q[f] << endl;
            if (f == r)
            {
                f = r = -1;
            }
            else
            {
                f++;
            }
        }
    }
    void delete_rear()
    {
        if (isempty() == 1)
        {
            cout << "queue is underflow " << endl;
        }
        else
        {
            cout << "deleted " << q[r] << endl;
            if (f == r)
            {
                f = r = -1;
            }
            else
            {
                r--;
            }
        }
    }
    void display()
    {
        for (int i = f; i <= r; i++)
        {
            cout << q[i] << " ";
        }
        cout << endl;
    }
};
int main()
{
    dequeue obj;
    int ch1, value;
    char ch;
    cout << "1)add at front\n2)add at rear\n3)delete front\n4)delete rear\n5)dislay\n"
         << endl;
    do
    {
        cout << "enter your ch  oice : ";
        cin >> ch1;
        switch (ch1)
        {
        case 1:
            cout << "enter the value that you want to add : ";
            cin >> value;
            obj.add_front(value);
            break;
        case 2:
            cout << "enter the value that you want to add : ";
            cin >> value;
            obj.add_rear(value);
            break;
        case 3:
            obj.delete_front();
            break;
        case 4:
            obj.delete_rear();
            break;
        case 5:
            obj.display();
            break;
        }
        cout << "do you want to continue (y/n) : ";
        cin >> ch;
    } while (ch == 'y');
    return 0;
}