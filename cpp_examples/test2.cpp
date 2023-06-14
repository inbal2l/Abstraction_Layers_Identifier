#include <sstream>
#include <ranges>

int main()
{
    std::istringstream iss ("0 1 2"); 
    for ( int i : rn::istream_view<int>( iss ) | rv::take(1) )
        std::cout << "j in loop: " << i << '\n';

    int j = 0;
    iss >> j;
    std::cout << "j after loop: " << j << '\n';
}
