$LanguageList = Get-WinUserLanguageList
$LanguageList.Add("ru-ru")
# $LanguageList.Remove($LanguageList[2])
$LanguageList.Add("en-gb")
$LanguageList.Remove(($LanguageList | Where-Object LanguageTag -like 'ru-ru'))
$LanguageList.Remove(($LanguageList | Where-Object LanguageTag -like 'en-gb'))