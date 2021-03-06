package room

type Repo struct {
	CFLEnd                         string `json:"CFLEnd"`
	CFLStart                       string `json:"CFLStart"`
	CFLVaryStep                    string `json:"CFLVaryStep"`
	DESType                        string `json:"DESType"`
	MUSCLCoefXk                    string `json:"MUSCLCoefXk"`
	TorqueRefX                     string `json:"TorqueRefX"`
	TorqueRefY                     string `json:"TorqueRefY"`
	TorqueRefZ                     string `json:"TorqueRefZ"`
	Aircoeffile                    string `json:"aircoeffile"`
	AngleSlide                     string `json:"angleSlide"`
	Attackd                        string `json:"attackd"`
	Axisup                         string `json:"axisup"`
	CatalyticCoef                  string `json:"catalyticCoef"`
	DumpQ                          string `json:"dump_Q"`
	FlowInitStep                   string `json:"flowInitStep"`
	ForceReferenceArea             string `json:"forceReferenceArea"`
	ForceReferenceLength           string `json:"forceReferenceLength"`
	ForceReferenceLengthSpanWise   string `json:"forceReferenceLengthSpanWise"`
	FreestreamVibrationTemperature string `json:"freestream_vibration_temperature"`
	FromGfile                      string `json:"from_gfile"`
	FromGtype                      string `json:"from_gtype"`
	Gasfile                        string `json:"gasfile"`
	GradientName                   string `json:"gradientName"`
	GridScaleFactor                string `json:"gridScaleFactor"`
	Gridfile                       string `json:"gridfile"`
	Gridtype                       string `json:"gridtype"`
	IfLowSpeedPrecon               string `json:"ifLowSpeedPrecon"`
	InflowParaType                 string `json:"inflowParaType"`
	InitMassFraction               string `json:"initMassFraction"`
	IntervalStepFlow               string `json:"intervalStepFlow"`
	IntervalStepForce              string `json:"intervalStepForce"`
	IntervalStepPlot               string `json:"intervalStepPlot"`
	IntervalStepRes                string `json:"intervalStepRes"`
	InviscidSchemeName             string `json:"inviscidSchemeName"`
	IsPlotVolumeField              string `json:"isPlotVolumeField"`
	Iunsteady                      string `json:"iunsteady"`
	Ktmax                          string `json:"ktmax"`
	LimitVariables                 string `json:"limitVariables"`
	LimitVector                    string `json:"limitVector"`
	MaxSimuStep                    string `json:"maxSimuStep"`
	MaxSubIter                     string `json:"max_sub_iter"`
	Maxproc                        string `json:"maxproc"`
	MinSubIter                     string `json:"min_sub_iter"`
	ModTurbRes                     string `json:"mod_turb_res"`
	NLUSGSSweeps                   string `json:"nLUSGSSweeps"`
	NMGLevel                       string `json:"nMGLevel"`
	NVisualVariables               string `json:"nVisualVariables"`
	NTurbScheme                    string `json:"n_turb_scheme"`
	Nchem                          string `json:"nchem"`
	Nchemrad                       string `json:"nchemrad"`
	Nchemsrc                       string `json:"nchemsrc"`
	Ntmodel                        string `json:"ntmodel"`
	OriginalGridFile               string `json:"original_grid_file"`
	OutGfile                       string `json:"out_gfile"`
	PartitionGridFile              string `json:"partition_grid_file"`
	PhysicalTimeStep               string `json:"physicalTimeStep"`
	Reconmeth                      string `json:"reconmeth"`
	RefDimensionalTemperature      string `json:"refDimensionalTemperature"`
	RefMachNumber                  string `json:"refMachNumber"`
	RefReNumber                    string `json:"refReNumber"`
	ResSaveFile                    string `json:"resSaveFile"`
	RestartNSFile                  string `json:"restartNSFile"`
	RoeEntropyFixMethod            string `json:"roeEntropyFixMethod"`
	RoeEntropyScale                string `json:"roeEntropyScale"`
	SpeciesName                    string `json:"speciesName"`
	StrLimiterName                 string `json:"str_limiter_name"`
	ToGtype                        string `json:"to_gtype"`
	TolSubIter                     string `json:"tol_sub_iter"`
	TurbInterval                   string `json:"turbInterval"`
	TurbMinCoef                    string `json:"turb_min_coef"`
	Turbfile                       string `json:"turbfile"`
	Turbresfile                    string `json:"turbresfile"`
	UnsLimiterName                 string `json:"uns_limiter_name"`
	UnsSchemeName                  string `json:"uns_scheme_name"`
	UnsVisName                     string `json:"uns_vis_name"`
	VenkatCoeff                    string `json:"venkatCoeff"`
	ViscousName                    string `json:"viscousName"`
	ViscousType                    string `json:"viscousType"`
	VisualVariables                string `json:"visualVariables[]"`
	Visualfile                     string `json:"visualfile"`
	WallTemperature                string `json:"wallTemperature"`
	WallAircoefile                 string `json:"wall_aircoefile"`
}
