int main()
{
    int i = 0;
    // std::cout << &i;			// 0x7ffc8584085c
    *(int*)0x7ffc8584085c = 1;	// UB
    return i;
}
