﻿namespace Main.Domains;

public class Player
{
#pragma warning disable CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
    public string Name { get; set; } = string.Empty;
    public string Country { get; set; }
    public string Tag { get; set; } = nameof(Tag);
    public string Character { get; set; } = nameof(Character);
    public string Sponsor { get; set; } = string.Empty;
    public int Counter { get; set; } = 0;

    public string FullName
    {
        get
        {
            return string.Concat(this.Tag, " | ", this.Name);
        }
    }
}