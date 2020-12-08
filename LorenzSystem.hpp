#ifndef __LorenzSystem__
#define __LorenzSystem__
#include <vector>
#include "DifferentialEquation.hpp"
using namespace std;

class LorenzSystem : public DifferentialEquation {
    private:
        double sigma;   // Prandtl number
	double rho;     // Rayleigh number
	double beta;    // Geometric factor

    public:
	// Constructors
	LorenzSystem() { }
	LorenzSystem(double s, double r, double b);
	
	// Accessor Methods
	double getSigma() { return sigma; }
	double getRho() { return rho; }
	double getBeta() { return beta; }
	
	// Mutator Methods
	void setSigma(double s) { sigma = s; }
	void setRho(double r) { rho = r; } 
	void setBeta(double b) { beta = b; }

	// Differential Equation
	vector<double> equation(vector<double> y, double t);
};

LorenzSystem::LorenzSystem(double s, double r, double b) {
    sigma = s;
    rho = r;
    beta = b;
}


/* Differential Equation of Lorenz Attractor
 *     dx/dt = sigma*(y - z)
 *     dy/dt = x*(rho - z) - y
 *     dz/dt = x*y - beta*z
 */
vector<double> LorenzSystem::equation(vector<double> y, double t) {
    vector<double> yp(3);
    yp.at(0) = sigma*(y.at(1) - y.at(0));
    yp.at(1) = y.at(0)*(rho - y.at(2)) - y.at(1);
    yp.at(2) = y.at(0)*y.at(1) - beta*y.at(2);
    return yp;    
}

#endif
