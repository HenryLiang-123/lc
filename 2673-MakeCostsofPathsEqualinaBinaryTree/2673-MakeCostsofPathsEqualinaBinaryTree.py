// Last updated: 2/28/2025, 2:51:49 PM
    for(int i=1;i<N/2;i++)
    {
        ans+= Math.abs(cost[i*2+1]-cost[i*2+2]);
    }
    return ans;
}