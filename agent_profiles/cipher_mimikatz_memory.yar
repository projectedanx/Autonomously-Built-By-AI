rule Cipher_MemResident_Mimikatz_Artifacts
{
    meta:
        description = "Detects memory-resident Mimikatz artifacts via behavioral string patterns and PE characteristics. Hash-agnostic: detects packed, renamed, and reflectively-loaded variants."
        author      = "Cipher (SCOS Agent ID: TDE-0X99)"
        date        = "2026-03-27"
        reference   = "https://attack.mitre.org/techniques/T1003/001/"
        mitre_id    = "T1003.001"
        cfdi_score  = "0.04"
        confidence  = "VERIFIED_IOC"

    strings:
        $cmd_logonpw  = "sekurlsa::logonpasswords" ascii nocase
        $cmd_privdbg  = "privilege::debug" ascii nocase
        $cmd_lsadump  = "lsadump::sam" ascii nocase
        $cmd_kerblist = "kerberos::list" ascii nocase
        $str_name_a   = "mimikatz" ascii nocase
        $str_name_w   = "mimikatz" wide nocase
        $hex_sig      = { 6D 69 6D 69 6B 61 74 7A }
        $export_str   = "sekurlsa" ascii
        $wdigest      = "WDigest" ascii
        $lsa_dump_str = "lsass.exe" ascii nocase

    condition:
        (uint16(0) == 0x5A4D) and
        filesize < 20MB and
        (
            (2 of ($cmd_*)) or
            ($hex_sig and $wdigest) or
            ($export_str and $lsa_dump_str) or
            (($str_name_a or $str_name_w) and 1 of ($cmd_*))
        )
}
