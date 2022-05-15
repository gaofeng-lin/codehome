package models

type Dbsettings struct{
	Dbname string
	Host string
	Port float64
	Password string
}
type Config struct{
	AesKey string
	Dbsettings Dbsettings
}