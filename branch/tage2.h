#include "ooo_cpu.h"
#include <cstdlib>
#include <bitset>
#include <stdlib.h>  
#include <cmath>


#define BIMODAL_TABLE_SIZE 4096
#define BANK_TABLE_SIZE 1024
#define GLOBAL_HISTORY_LENGTH 80
#define NO_OF_BANKS 4
#define NO_OF_BITS_BIMODAL_COUNTER 2
#define NO_OF_BITS_BANK_COUNTER 3 
#define BANK_INDEX_SIZE 10

//const int bank_sizes[] = {10,11,11,11,10,10,10,9,9} ; 
const int bank_ghr_sizes[] = {4,6,11,16,25,40,64,101,160,254,403,640} ; 
// const int bank_ghr_sizes[] = {10,20,40,80} ;
const int tag_sizes[] = {8,8,8,8} ;

// int global_history[GLOBAL_HISTORY_LENGTH];
bitset<GLOBAL_HISTORY_LENGTH> GHR;
bitset<GLOBAL_HISTORY_LENGTH> temp;
bitset<GLOBAL_HISTORY_LENGTH> mask;
bitset<GLOBAL_HISTORY_LENGTH> CSR1_mask;
bitset<GLOBAL_HISTORY_LENGTH> CSR2_mask;




// Track X bank
int bank_chosen,alt_bank;
int bank_pred,alt_pred;
int tag;

int ind[NO_OF_BANKS+1] ; 

class BimodalCell {
    public:
    int counter;
    int msb;
    int max_val ; 

    BimodalCell() {
        max_val = pow(2,NO_OF_BITS_BIMODAL_COUNTER)-1 ; 
        this->counter = pow(2,NO_OF_BITS_BIMODAL_COUNTER-1) ;
        this->msb = 1;
    }

    void increment() {
        if (counter < max_val) {
            counter++;
            this->msb = (counter >> (NO_OF_BITS_BIMODAL_COUNTER-1));
        }
    }

    void decrement() {
        if (counter > 0) {
            counter--;
            this->msb = (counter >> (NO_OF_BITS_BIMODAL_COUNTER-1));
        }
    }

    void update(int counter) {
        this->counter = counter;
        this->msb = (counter >> (NO_OF_BITS_BIMODAL_COUNTER-1));
    }
};

class BankCell {
    public: 
    int counter;
    int tag;
    int u;
    int msb;

    void Bankcell() {
        this->counter = pow(2,NO_OF_BITS_BANK_COUNTER-1);
        this->tag = 0;
        this->u = 0;
        this->msb = 1;
    }

    void increment() {
        if (counter < pow(2,NO_OF_BITS_BANK_COUNTER)-1 ) {
            counter++;
            this->msb = (counter >> (NO_OF_BITS_BANK_COUNTER-1));
        }
    }

    void decrement() {
        if (counter > 0) {
            counter--;
            this->msb = (counter >> (NO_OF_BITS_BANK_COUNTER-1));
        }
    }

    void increment_u() { 
          if ( this->u < 3 ){ 
              this->u += 1 ; 
          }
    }
    void decrement_u() { 
          if ( this->u > 0 ){ 
              this->u -= 1  ; 
          }
    }
    void update(int tag, int counter) {
        this->counter = counter;
        this->tag = tag;
        this->u = 0 ;
        this->msb = (counter >> (NO_OF_BITS_BANK_COUNTER-1));
        // //cout<< int(counter) << " bank msb " << int(this->msb) << endl;
    }
};

class BimodalTable {
    public:
    BimodalCell* bimodaltable[BIMODAL_TABLE_SIZE];

    BimodalTable() {
        for(int i = 0; i < BIMODAL_TABLE_SIZE; i++) {
            bimodaltable[i] = new BimodalCell();
        }
    }

    BimodalCell* getindex(int index) {
        return bimodaltable[index];
    }

    void update_counter(int index, int taken) {
        int bank_ctr = bimodaltable[index]->counter;
        if (taken) {
                bimodaltable[index]->increment();
        } else {
                bimodaltable[index]->decrement();
        }
    }

    void print() { 
         for ( int i = 0 ; i < BIMODAL_TABLE_SIZE ; i++ ) { 
              if ( bimodaltable[i]->counter  != 2 || bimodaltable[i]->msb != 1 ) { 
                  //cout<<i<<" "<<int(bimodaltable[i]->counter)<<" "<< int(bimodaltable[i]->msb) <<endl ; 
              }
         }
         //cout<<"End"<<endl;
    }
};

class BankTable {
    public:
    BankCell* banktable[BANK_TABLE_SIZE];
    int bankNo;
    bitset<GLOBAL_HISTORY_LENGTH> history_mask_1;
    bitset<GLOBAL_HISTORY_LENGTH> history_mask_2;
    bitset<GLOBAL_HISTORY_LENGTH> history_mask_3;
    bitset<GLOBAL_HISTORY_LENGTH> history_mask_4;
    bitset<GLOBAL_HISTORY_LENGTH> temp_2;
    int ghr_index_size,middle_range , last_range ,tag_size ; 
   
    BankTable(int bankNo, int ghr_index_size , int tag_size) {
        this->bankNo = bankNo;
        this->tag_size = tag_size ; 
        for(int i = 0; i < BANK_TABLE_SIZE; i++) {
            banktable[i] = new BankCell();
        }

        history_mask_1.reset();
        history_mask_2.reset();
        history_mask_3.reset();
        history_mask_4.reset();
        for (int i = 0; i < GLOBAL_HISTORY_LENGTH; i++) {
              if (i > BANK_INDEX_SIZE-1) {
                 history_mask_1.set(i, 0);
             } else {
                 history_mask_1.set(i, 1);
             }
         }
         this->ghr_index_size = ghr_index_size ; 
         middle_range = ghr_index_size / BANK_INDEX_SIZE;
         last_range = ghr_index_size % BANK_INDEX_SIZE ;
         for (int i = 0; i < GLOBAL_HISTORY_LENGTH; i++) {
             if (i > last_range-1) {
                 history_mask_2.set(i, 0);
             } else {
                 history_mask_2.set(i, 1);
             }
         }

         for (int i = 0; i < GLOBAL_HISTORY_LENGTH; i++) {
             if (i > tag_size-1) {
                   history_mask_3.set(i, 0);
             } else {
                  history_mask_3.set(i, 1);
             }
          }
          for (int i = 0; i < GLOBAL_HISTORY_LENGTH; i++) {
             if (i > tag_size-2) {
                   history_mask_4.set(i, 0);
             } else {
                  history_mask_4.set(i, 1);
             }
          }
   
    }

    uint64_t get_tag( uint64_t ip ) {
       uint64_t tag = 0;
       tag = ip & ((1 << tag_size) - 1);
       temp = GHR;
       tag = tag ^ (temp &= history_mask_3).to_ulong();
       temp = GHR;
       temp >>= tag_size;
       tag = tag ^ ((temp &= history_mask_4).to_ulong() << 1);
       return tag;
    }

    uint64_t return_index( uint64_t ip ) {
        uint64_t index = 0;
        index = ip & ((1 << BANK_INDEX_SIZE) - 1);
        
        temp_2 = GHR;
        for (int i = 0; i < middle_range; i++) {
            index = index ^ (temp_2 &= history_mask_1).to_ulong();
            temp_2 = GHR;
            temp_2 >>= BANK_INDEX_SIZE*(i+1);
        }
        index = index ^ (temp_2 &= history_mask_2).to_ulong();
        temp_2 = GHR;
        return index;
    }

    BankCell* getindex(int index) {
        return banktable[index];
    }

    void update_counter(int index, int taken) {
        int bank_ctr = banktable[index]->counter;
        if (taken) {
            banktable[index]->increment();
        } else {
            banktable[index]->decrement();
        }
        ////cout<<"Bank "<<(this->bankNo)<<" index "<<int(index)<<" tag "<<tag<<" counter "<<int(banktable[index]->counter)<<endl  ; 
    }
    
    void update( int index, int tag ) {
        banktable[index]->update(tag, pow(2,NO_OF_BITS_BANK_COUNTER-1) );
    }

    void print() { 
         //cout<<"Bank Table "<<int(this->bankNo)<<endl ; 
         for ( int i = 0 ; i < BANK_TABLE_SIZE ; i++ ) { 
              if ( banktable[i]->tag  != 0 ) { 
                  //cout<<i<<" "<<int(banktable[i]->counter)<<" "<<int(banktable[i]->tag)<<" "<<int(banktable[i]->u)<<endl ; 
              }
         }
         //cout<<"End"<<endl;
    }
};

class Tables { 
    public : 
     BimodalTable* bimodal_table;
     BankTable* banks[NO_OF_BANKS] ; 
     Tables() { 
         for ( int i = 0 ; i < NO_OF_BANKS ; i ++ ) banks[i] = new BankTable(i+1,bank_ghr_sizes[i],tag_sizes[i]) ; 
         bimodal_table = new BimodalTable(); 
     }
     
     void update_counter(int bank_chosen , int taken) {  //bank_chosen 
           if ( bank_chosen ) banks[bank_chosen-1]->update_counter(ind[bank_chosen] , taken );
           else bimodal_table->update_counter(ind[bank_chosen] , taken ) ; 
     }

     void add_new_entry_miss( int bank_chosen  , int taken) { 
          
          if ( bank_chosen == NO_OF_BANKS) return ; 
          int is_all_u_set = true ; 
          int count = 0 ;

          for ( int i = bank_chosen + 1 ; i <=NO_OF_BANKS  ; i++ ) {  
                if ( !banks[i-1]->getindex(ind[i])->u ) { 
                      //banks[i-1]->update( ind[i] , tag);
                      is_all_u_set = false ; 
                      count++;
                      //break ; 
                }
          }

          if ( count ) { 
               int rand_bank = (rand()%count) + 1    ; //1 to 2^n-1  
               int k = 1 ; 
               for ( int i = bank_chosen + 1 ; i <=NO_OF_BANKS  ; i++ ) {  
                if ( !banks[i-1]->getindex(ind[i])->u ) {
                      if ( rand_bank == k ) {    
                          banks[i-1]->update( ind[i] , tag);
                          break ;
                      }
                      k += 1 ; 
                  }
             }
          } 
        //     int exp_weight = 2 ; 
        //     int rand_bank = (rand()%int( pow(exp_weight,count)-1 )) + 1    ; //1 to 2^n-1  
        //     int j = pow(exp_weight,count-1) ; // 2^(n-1) 
        //     int k = count - 1 ; 
        //     for ( int i = bank_chosen + 1 ; i <=NO_OF_BANKS  ; i++ ) {  
        //       if ( !banks[i-1]->getindex(ind[i])->u ) {
        //             if ( rand_bank <= j ) {    
        //                 banks[i-1]->update( ind[i] , tag);
        //                 break ;
        //             }
        //             k--;
        //             j += pow(exp_weight,k); 
        //        }
        //     }
        //   }

          if ( is_all_u_set ) { 
               for ( int i = bank_chosen + 1 ; i <=NO_OF_BANKS ; i++ ) { 
                   banks[i-1]->getindex(ind[i])->decrement_u();
               }
          }  
     }
    
     void updateIndex( uint64_t ip ) { 
        temp = GHR;
        ind[0] = (ip & ~(~0 << 12));
        for ( int i = 0 ; i < NO_OF_BANKS ; i++ ) {
           ind[i+1] = banks[i]->return_index(ip);
        }

        // int index1 = (ip & ~(~0 << 10)) ^ (temp &= mask).to_ulong();
        // temp = GHR;
        // temp >>= 10;
        // int index2 = index1 ^ (temp &= mask).to_ulong();
        // temp = GHR;
        // temp >>= 20;
        // int index3 = index2 ^ (temp &= mask).to_ulong();
        // temp = GHR;
        // temp >>= 30;
        // index3 = index3 ^ (temp &= mask).to_ulong();
        // temp = GHR;
        // temp >>= 40;
        // int index4 = index3 ^ (temp &= mask).to_ulong();
        // temp = GHR;
        // temp >>= 50;
        // index4 = index4 ^ (temp &= mask).to_ulong();
        // temp = GHR;
        // temp >>= 60;
        // index4 = index4 ^ (temp &= mask).to_ulong();
        // temp = GHR;
        // temp >>= 70;
        // index4 = index4 ^ (temp &= mask).to_ulong();
        // ind[1] = index1 ; 
        // ind[2] = index2 ; 
        // ind[3] = index3 ; 
        // ind[4] = index4 ; 
     }
    
     void findPred(uint64_t tag) {
          bank_pred = bimodal_table->getindex(ind[0])->msb ;  
          bank_chosen = 0 ; 

          for ( int i = NO_OF_BANKS-1  ; i >= 0 ; i-- ) {  //bank_chosen  = i + 1 
              if ( banks[i]->getindex(ind[i+1])->tag == tag ){ //banks[i]->get_tag(ip) ) {
                   bank_chosen = i+1 ; 
                   bank_pred = banks[i]->getindex(ind[i+1])->msb ; 
                   break ;  
              }
          }
         
          alt_pred = bimodal_table->getindex(ind[0])->msb ;  
          alt_bank = 0 ;
          if ( bank_chosen > 1 ) {  
            for ( int i = bank_chosen-2  ; i >= 0 ; i-- ) {  //bank_chosen  = i + 1 
               if ( banks[i]->getindex(ind[i+1])->tag == tag ) { //banks[i]->get_tag(ip) ) {
                   alt_bank = i+1 ; 
                   alt_pred = banks[i]->getindex(ind[i+1])->msb ; 
                   break ;  
               }
            }
         }

         cout << bank_chosen << endl;

     }
  
     void print() { 
         bimodal_table->print();
         for ( int i = 0 ; i < NO_OF_BANKS ; i++ ) banks[i]->print();
     }
}; 

class Tage {
public:
    Tables tables ;

// 4 bits -> 3 for counter, 1 for m

// 12 bits -> 3 for counter, 8 for tag, 1 for u

    BimodalCell* ab = tables.bimodal_table->getindex(1503) ; 

    Tage() {
        
        for(int i = 0; i < GLOBAL_HISTORY_LENGTH; i++) {
            if (i > 9) {
                mask.set(i, 0);
            } else {
                mask.set(i, 1);
            }

            if (i > 7) {
                CSR1_mask.set(i, 0);
            } else {
                CSR1_mask.set(i, 1);
            }
            
            if (i > 6) {
                CSR2_mask.set(i, 0);
            } else {
                CSR2_mask.set(i, 1);
            }
        }

        bank_chosen = 0;
        bank_pred = 0;
        tag = 0;

        GHR.reset();
        temp.reset();

    }
    
    uint8_t predict(uint64_t ip) {
        tables.updateIndex(ip);
        //tag find start 
        temp = GHR;
        tag = (ip & ~(~0 << 8)) ^ (temp &= CSR1_mask).to_ulong();
        temp = GHR;
        temp >>= 8;
        tag = tag ^ ((temp &= CSR2_mask).to_ulong() << 1);
        tables.findPred(tag);
        //cout<<"Start"<<endl ; 
        //cout<<tag<<endl ; 
        //cout<<( tables.banks[0]->get_tag(ip) )<<endl  ;
        //cout<<( tables.banks[1]->get_tag(ip) )<<endl ;
        //cout<<( tables.banks[2]->get_tag(ip) )<<endl ;
        //cout<<( tables.banks[3]->get_tag(ip) )<<endl ;
        return bank_pred ;  
    }

    void last_branch_result(uint16_t ip, uint8_t taken) {
        //srand(1);
        GHR = (GHR << 1);
        GHR.set(0, taken);

        // update counter for the predictor bank with respect whether the branch is taken 
        tables.update_counter(bank_chosen  , taken);

        // X <= 3
        if ( bank_pred != taken) {
            tables.add_new_entry_miss( bank_chosen , taken );
        }

        if ( bank_chosen && (bank_pred != alt_pred) ) { 
                if ( bank_pred == taken ) tables.banks[ bank_chosen - 1 ]->getindex(ind[bank_chosen])->increment_u(); 
                else tables.banks[ bank_chosen - 1 ]->getindex(ind[bank_chosen])->decrement_u() ; 
        }

        //cout<<"update"<<endl;   
        //cout<<"x :: "<<int(bank_pred)<<" "<<int(alt_pred)<<" "<<int(taken)<<" "<<endl ; 
        tables.print();
    }
    
    
};