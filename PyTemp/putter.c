/**
 * Compilation command 
 * gcc -O2 putter.c -o cputter -lpdi -lparaconf
 * */

#include <stdio.h>
#include <stdlib.h>
#include <pdi.h>
int main(int argc, char const *argv[])
{
    PC_tree_t node = PC_parse_path("env.yml");
    PDI_init(PC_get(node, ".pdi"));

    int RUN = 1;
    int HASN = 0;
    float SIM_FERT_VAL[4];

    PDI_expose("RUN_SE", &RUN, PDI_IN);
    while (RUN)
    {
        PDI_expose("RL_FERT_VAL", SIM_FERT_VAL, PDI_IN);
        printf("RL_FERT_VAL[0]: %f\n", SIM_FERT_VAL[0]);

        PDI_expose("HASN", &HASN, PDI_OUT);
        printf("C HASN: %d\n", HASN);

        PDI_expose("RUN_SE", &RUN, PDI_IN);

        RUN = HASN < 20 ? RUN : 0;
        HASN++;
    }

    PDI_finalize();

    return 0;
}
