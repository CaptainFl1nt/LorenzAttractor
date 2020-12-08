#include <iostream>
#include <fstream>
#include <vector>
#include "LorenzSystem.hpp"
#include "RungeKuttaSolver.hpp"
using namespace std;

int main() {
    // open data file
    ifstream infile;
    infile.open("input.txt");

    // get output file name
    string filename;
    getline(infile,filename,'\n');

    // read data
    double dt, Tmax, sigma, rho, beta;
    vector<double> y0(3);
    infile >> dt >> Tmax >> sigma >> rho >> beta;
    infile >> y0.at(0) >> y0.at(1) >> y0.at(2);
    
    // set up system and solver
    LorenzSystem system = LorenzSystem(sigma,rho,beta);
    RungeKuttaSolver solver = RungeKuttaSolver(&system, y0);
    solver.setDt(dt);
    solver.setTMax(Tmax);

    // run and save simulation
    solver.Solve();
    solver.output(filename);
    return 0;
}
