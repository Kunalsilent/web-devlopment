#include <iostream>
using namespace std;
void shellsort(int a[], int n)
{
    for (int gap = n / 2; gap > 0; gap /= 2)
    {
        for (int i = gap; i < n; i += 1)
        {
            int temp = a[i];
            int j;
            for (j = i; j >= gap && a[j - gap] > temp; j -= gap)
                a[j] = a[j - gap];
            a[j] = temp;
        }
    }
}

void insertionsort(int a[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int smaller = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > smaller)
        {
            a[j + 1] = a[j];
            j = j - 1;
        }
        a[j + 1] = smaller;
    }
}
void display(int a[],int n)
{
    for (int i = 0; i < n; i++)
    {
        cout<<a[i];
    }

}
int main()
{
    int n;
    cout << "enter the number of element required";
    cin >> n;
    int a[n];
    cout << "enter the value for array";
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << "enter the choice for sorting 1 for shell sort 2 for insertion sort " << endl;
    int c;
    cin >> c;
    switch (c == 1)
    {
    case 1:
        insertionsort(a, n);

        break;

    default:
        shellsort(a, n);
        break;

    }
    display(a,n);

}