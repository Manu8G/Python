void reestructuraRaiz(double *apo, int pos, int tamapo){
    int minhijo;
    if(2*pos+1 < tamapo){
        minhijo=2*pos+1;
        if((minhijo+1 < tamapo) && (apo[minhijo]>apo[minhijo+1]))minhijo++;
        if(apo[pos]>apo[minhijo]){
            double tmp = apo[pos];
            apo[pos]=apo[minhijo];
            apo[minhijo]=tmp;
            reestructuraRaiz(apo, minhijo, tamapo);
        }
    }
}

int main(int argc, char *argv[]){
    double apo=[4, 5, 2, 6, 7, 8, 2, 3, 1, 9];
    int pos=argv[1];
    reestructuraRaiz(apo, pos, len(apo));
}