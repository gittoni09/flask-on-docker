//Auxiliary functions for the NumberGuesser game
function NumGen()
	{
	// Random number is generated everytime the page loads
	var myNumber = Math.round(Math.random() * 100);
	return myNumber;
	}

//Auxiliary functions for the MissingNumber game
function OperationSelector()
	{
	
	var myNumber = Math.round(Math.random() * 10);
	if (myNumber > 5)
		{
			return "+";
		} 
	else
		{
			return "-";
		}
	
	}

function GenOp (OpSign)
	{

	var op1 = Math.round(Math.random() * 100);
	var op2 = Math.round(Math.random() * 100);
	var op3 = 0;
	if (op2 > op1) //If op2 > op1 the values are exchanged to avoid negative results
		{
		 op3 = op1;
		 op1= op2;
		 op2 = op3;
		}
	
	if (OpSign == "+")
		{
			return op1 +";+;" + op2 + "; = [ ] ";
		} 
	else 
		{
			return op1 + ";-;" + op2 + "; = [ ] ";
		} 	
	}
