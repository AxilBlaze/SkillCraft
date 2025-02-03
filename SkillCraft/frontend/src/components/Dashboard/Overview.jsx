import React, { useEffect } from 'react';
import { useApi } from '@/hooks/useApi';
import { dashboardService } from '@/services/dashboard';

const DashboardOverview = () => {
  const { data, error, loading, execute: fetchOverview } = useApi(dashboardService.getOverview);

  useEffect(() => {
    fetchOverview();
  }, [fetchOverview]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!data) return null;

  return (
    <div>
      <h2>Dashboard Overview</h2>
      <div>Progress: {data.progress}</div>
      <div>Recommendations: {data.recommendations?.length || 0}</div>
      <div>Skill Gaps: {data.skill_gaps?.length || 0}</div>
    </div>
  );
};

export default DashboardOverview; 