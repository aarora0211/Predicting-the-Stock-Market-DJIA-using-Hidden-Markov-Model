#Akshit Arora, Sheershak Agarwal
#Tests the algorithm with the default obersvations
#Interactive application, user can also enter 

import HMM as hmm
import DataSet as data

if __name__ == "__main__":
        print('Do you want to run the default test?')
        default = input('Y/N: ')
        if default == 'Y':
                forward = hmm.forward(data.obs, data.states, data.start_prob, data.transition_prob, data.emission_prob)
                prob, viterbi = hmm.viterbi(data.obs, data.states, data.start_prob, data.transition_prob, data.emission_prob)
                print("The predicted probability by the forward algorithm is: " + str(forward) + "\n")
                print("The predicted best path by the viterbi algorithm is: " + str(viterbi) + "\n")
                print("The predicted best path probability of algorithm is: " + str(prob) + "\n")

        elif(default == 'N'):
                value = input('Your input operation (Invest,Do_Not_Invest,Your_Choice(delemiter = ,)): ')
                obs = value.split(',')
                forward = hmm.forward(obs, data.states, data.start_prob, data.transition_prob, data.emission_prob)
                prob, viterbi = hmm.viterbi(obs, data.states, data.start_prob, data.transition_prob, data.emission_prob)
                print("The predicted probability by the forward algorithm is: " + str(forward) + "\n")
                print("The predicted best path by the viterbi algorithm is: " + str(viterbi) + "\n")
                print("The predicted best path probability of algorithm is: " + str(prob) + "\n")
