#include <stdio.h>
#include <pdi.h>
int main(int argc, char const *argv[])
{
    PC_tree_t node = PC_parse_path("put.yml");
    PDI_init(PC_get(node, ".pdi"));

    int RUN=1;
    int HASN = 0;
    PDI_expose("RUN_SE", &RUN, PDI_IN);
    while (RUN) {
        PDI_expose("HASN", &HASN, PDI_OUT);
        printf("C HASN: %d\n", HASN);

        PDI_expose("RUN_SE", &RUN , PDI_IN);
        HASN++;
    }

    PDI_finalize();

    return 0;
}
