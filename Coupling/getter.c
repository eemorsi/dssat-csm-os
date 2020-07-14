#include <stdio.h>
#include <pdi.h>
int main(int argc, char const *argv[])
{
    PC_tree_t node = PC_parse_path("get.yml");
    PDI_init(PC_get(node, ".pdi"));

    int RUN;
    int HASN;
    PDI_expose("RUN_SE", &RUN, PDI_IN);
    while (RUN) {
        printf("C: from the while loop\n");

        PDI_expose("HASN", &HASN, PDI_IN);
        printf("HASN: %d\n", HASN);
        
        PDI_expose("RUN_SE", &RUN , PDI_IN);
    }

    PDI_finalize();
    return 0;
}
