echo 'CGenFF (single topology file)\n'
../bin/validate.py 1-bromobutane.wfn 1-bromobutane_cgenff.itp
echo 'OPLS (loading dependency)\n'
../bin/validate.py 1-bromobutane.wfn 1-bromobutane_opls.itp
